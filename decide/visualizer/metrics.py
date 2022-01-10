from decide import voting
from models import Vote  
from voting.models import Voting

def listVotes():
    return Vote.objects.all()

def votesOfVoting(v_id):
    return Vote.objects.filter(voting_id = v_id).count()

def unstartedVotings():
    return Voting.objects.filter(start_date__isnull=True).count()

def startedVotings():
    return Voting.objects.filter(start_dateisnull=False).count()

def finishedVotings():
    return Voting.objects.filter(end_dateisnull=False, tallyisnull=False).count()

def closedVotings():
    return Voting.objects.filter(end_dateisnull=False, tally__isnull=True).count()

