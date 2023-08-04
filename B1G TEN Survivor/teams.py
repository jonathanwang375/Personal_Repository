import participants
import openpyxl
from dataclasses import dataclass
from typing import List

@dataclass
class Team:
    name: str
    wins: int
    losses: int

BigTenTeamNameList = ["Illinois", "Indiana", "Iowa", "Maryland", "Michigan", "Michigan State", "Minnesota", "Nebraska", "Northwestern", "Ohio State", "Penn State", "Purdue", "Rutgers", "Wisconsin"]
BigTenTeamList: List[Team]

def initialize_list():
    #create a the Big 10 Team List
    Big10TeamList = []
    for team in BigTenTeamNameList:
        Big10TeamList.append(Team(name=team, win=0, loss=0))

def add_a_loss(team_name: str):
    #increment a loss for a given team
    test = False
    for team in BigTenTeamList:
        if team.name == team_name:
            losses = losses + 1
    participants.check_team_status(team_name, False)

def add_a_win(team_name: str):
    #increment a win for a given team
    for team in BigTenTeamList:
        if team.name == team_name:
            wins = wins + 1
    participants.check_team_status(team_name, True)