import teams
import openpyxl
from dataclasses import dataclass
from typing import List

@dataclass
class WeekSelection:
    team_chosen: teams.Team
    week_number: int

@dataclass
class Person:
    name: str
    selections: List[WeekSelection]
    eliminated: bool
    last_week: int
    overall_wins: int
    overall_loss: int
    place: int

ParticipantList: List[Person]
NameList: List

def set_overall_record():
    #set the overall record for each person
    for person in ParticipantList:
        overall_win = 0
        overall_loss = 0
        for team_selection in person.selections:
            overall_win = overall_win + team_selection.team_chosen.win
            overall_loss = overall_loss + team_selection.team_chosen.loss
        person.overall_wins = overall_win
        person.overall_loss = overall_loss

def check_team_status(team_name: str, loss: bool):
    #if the team won, check to see who selected team. anyone who selected the team moves on
    #if the team loss, check to see who selected team. anyone who selected the team is eliminated
    #update the records of everyone 
    test = False
    if loss:
        for person in ParticipantList:
            if person.selections[len(person.selections) - 1] == team_name:
                person.eliminated = True
    for person in ParticipantList:
        for team_selected in person.selections.team_chosen:
            for BIGTenTeam in teams.BigTenTeamList:
                if team_selected.name == BIGTenTeam.name:
                    team_selected.wins = BIGTenTeam.wins
                    team_selected.losses = BIGTenTeam.losses
    set_overall_record()
    determine_place()

def add_participants():
    #add players to the list, edit players' name, delete players' name and finalize list
    test = False

def determine_place():
    #this will determine the place of each player and reshuffle the list based off of that
    test = False

def add_team_guess(participant_name: str, team_name: str):
    #add the team to the end of list when someone makes a guess
    test = False

def change_team_guess(participant_name: str, new_team_name: str):
    #change the name of the team when a player wants to
    test = False