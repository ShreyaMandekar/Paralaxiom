import os
import django
import pandas as pd
from datetime import datetime

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipl_project.settings')
django.setup()

from ipl_api.models import Match, Delivery

# Clear existing data
Match.objects.all().delete()
Delivery.objects.all().delete()

# Load CSV files
matches_df = pd.read_csv('./data/matches.csv')
deliveries_df = pd.read_csv('./data/deliveries.csv')

# Load Matches
match_objects = []
for _, row in matches_df.iterrows():
    match_objects.append(Match(
        match_id=row['id'],  # store original ID as match_id
        season=row['season'],
        city=row.get('city', ''),
        date=pd.to_datetime(row['date']).date(),
        team1=row['team1'],
        team2=row['team2'],
        toss_winner=row.get('toss_winner', ''),
        toss_decision=row.get('toss_decision', ''),
        result=row.get('result', ''),
        dl_applied=row.get('dl_applied', 0),
        winner=row.get('winner', ''),
        win_by_runs=row.get('win_by_runs', 0),
        win_by_wickets=row.get('win_by_wickets', 0),
        player_of_match=row.get('player_of_match', ''),
        venue=row.get('venue', ''),
        umpire1=row.get('umpire1', ''),
        umpire2=row.get('umpire2', ''),
        umpire3=row.get('umpire3', '')
    ))

Match.objects.bulk_create(match_objects)

# Create a dictionary for match lookup
match_lookup = {m.match_id: m for m in Match.objects.all()}

# Load Deliveries
delivery_objects = []
for _, row in deliveries_df.iterrows():
    match = match_lookup.get(row['match_id'])
    if match:
        delivery_objects.append(Delivery(
            match=match,
            inning=row['inning'],
            batting_team=row['batting_team'],
            bowling_team=row['bowling_team'],
            over=row['over'],
            ball=row['ball'],
            batsman=row['batsman'],
            non_striker=row['non_striker'],
            bowler=row['bowler'],
            batsman_runs=row['batsman_runs'],
            extra_runs=row['extra_runs'],
            total_runs=row['total_runs'],
            is_super_over=row.get('is_super_over', 0),
            wide_runs=row.get('wide_runs', 0),
            bye_runs=row.get('bye_runs', 0),
            legbye_runs=row.get('legbye_runs', 0),
            noball_runs=row.get('noball_runs', 0),
            penalty_runs=row.get('penalty_runs', 0),
            player_dismissed=row.get('player_dismissed', ''),
            dismissal_kind=row.get('dismissal_kind', ''),
            fielder=row.get('fielder', '')
        ))

Delivery.objects.bulk_create(delivery_objects)

print(" Data loaded successfully!")
print(f" Total matches: {Match.objects.count()}")
print(f" Total deliveries: {Delivery.objects.count()}")
