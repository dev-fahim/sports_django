import itertools
import math
import random
import typing
from pprint import pprint

from django.db.models import QuerySet

from sports.models import Event, Team, Group, Match, Venue


def get_all_events():
    return Event.objects.all()


def generate_fixture_table(event_id: int, groups: int, venues: QuerySet[Venue]):
    teams = Team.objects.all()
    total_teams = teams.count()
    team_list = list(teams)
    random.shuffle(team_list)

    venue_list = list(venues)
    random.shuffle(venue_list)

    per_match_opponents = 2

    current_match_count = 0
    for i in range(groups):
        # group = Group.objects.create(name=f'GROUP_{i+1}', event_id=event_id)
        print(f'GROUP_{i+1}')

        r = int(total_teams / groups)
        s = r * i
        e = s + r
        print(r, s, e)
        match_team_wise_combinations = []
        for j in itertools.combinations(team_list[s:e], per_match_opponents):
            match_team_wise_combinations.append(j)

        pprint(match_team_wise_combinations)

        total_matches_count = len(match_team_wise_combinations)

        for j in range(total_matches_count):
            # match = Match.objects.create(
            #     name=f'MATCH_{i+j+1}',
            #     venue_id=random.choice(venues).id,
            #     event_id=event_id,
            # )
            print(f'MATCH_{current_match_count+1}')
            current_match_count += (i + j)
            for k in range(2):
                team = match_team_wise_combinations[j][k]
                print(team.name)
                # team.group_id = group.id
                # team.save()
                # match.teams.add(team)
                # match.save()
