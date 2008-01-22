#include <memory>

// user include files
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"
#include "FastSimulation/Event/interface/FSimEvent.h"
#include "FastSimulation/Event/interface/FSimTrack.h"
#include "FastSimulation/Event/interface/FSimVertex.h"
#include "FastSimulation/Particle/interface/ParticleTable.h"

#include <iostream>

using namespace edm;
using namespace std;

//
// class decleration
//

class NuclearInteractionFilter : public edm::EDFilter {

 public:

  explicit NuclearInteractionFilter(const edm::ParameterSet&);
  ~NuclearInteractionFilter();
  
  virtual bool filter(Event&, const EventSetup&);
  virtual void beginJob(const edm::EventSetup & c);

 private:

  edm::ParameterSet vertexGenerator_;
  edm::ParameterSet particleFilter_;
  FSimEvent* mySimEvent;
};

NuclearInteractionFilter::NuclearInteractionFilter(const edm::ParameterSet& p) 
{  

  particleFilter_ = p.getParameter<edm::ParameterSet>
    ( "FilterParticleFilter" );   
  // For the full sim
  mySimEvent = new FSimEvent(particleFilter_);

}


NuclearInteractionFilter::~NuclearInteractionFilter()
{}

void NuclearInteractionFilter::beginJob(const edm::EventSetup & es)
{
  // init Particle data table (from Pythia)
  edm::ESHandle < HepPDT::ParticleDataTable > pdt;
  es.getData(pdt);
  if ( !ParticleTable::instance() ) ParticleTable::instance(&(*pdt));
  mySimEvent->initializePdt(&(*pdt));

}


bool NuclearInteractionFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  //  std::cout << "Fill full event " << std::endl;
  edm::Handle<std::vector<SimTrack> > fullSimTracks;
  iEvent.getByLabel("g4SimHits",fullSimTracks);
  edm::Handle<std::vector<SimVertex> > fullSimVertices;
  iEvent.getByLabel("g4SimHits",fullSimVertices);
  mySimEvent->fill( *fullSimTracks, *fullSimVertices );
  
  bool accepted = false;

  XYZTLorentzVector theProtonMomentum(0.,0.,0.,0.986);

  // There is only one vertex : reject
  if ( mySimEvent->nVertices() == 1 ) return accepted; 
  
  // Pion's number of daughters
  FSimVertex& thePionVertex = mySimEvent->vertex(1);
  unsigned ndaugh = thePionVertex.nDaughters();

  // First and last daughters
  int firstDaughter = -1;
  int lastDaughter = -1;
  if ( ndaugh ) { 
    lastDaughter = thePionVertex.daughters()[thePionVertex.nDaughters()-1];
    firstDaughter = thePionVertex.daughters()[0];
  } 

  // Reject pion decays (already simulated in FAMOS)
  if ( thePionVertex.nDaughters() == 1 ) { 
    FSimTrack myDaugh = mySimEvent->track(firstDaughter);
    if (abs(myDaugh.type()) == 11 || abs(myDaugh.type()) == 13 ) return accepted;
  } 

  accepted = true;
  return accepted;

}
//define this as a plug-in
DEFINE_SEAL_MODULE();
DEFINE_ANOTHER_FWK_MODULE(NuclearInteractionFilter);
