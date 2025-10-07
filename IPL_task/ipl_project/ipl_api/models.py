from django.db import models


class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    season = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    team1 = models.CharField(max_length=100, null=True, blank=True)
    team2 = models.CharField(max_length=100, null=True, blank=True)
    toss_winner = models.CharField(max_length=100, null=True, blank=True)
    toss_decision = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    dl_applied = models.IntegerField(null=True, blank=True)
    winner = models.CharField(max_length=100, null=True, blank=True)
    win_by_runs = models.IntegerField(null=True, blank=True)
    win_by_wickets = models.IntegerField(null=True, blank=True)
    player_of_match = models.CharField(max_length=100, null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    umpire1 = models.CharField(max_length=100, null=True, blank=True)
    umpire2 = models.CharField(max_length=100, null=True, blank=True)
    umpire3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.season} - {self.team1} vs {self.team2}"


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True)
    inning = models.IntegerField(null=True, blank=True)
    batting_team = models.CharField(max_length=100, null=True, blank=True)
    bowling_team = models.CharField(max_length=100, null=True, blank=True)
    over = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField(null=True, blank=True)
    batsman = models.CharField(max_length=100, null=True, blank=True)
    non_striker = models.CharField(max_length=100, null=True, blank=True)
    bowler = models.CharField(max_length=100, null=True, blank=True)
    is_super_over = models.IntegerField(default=0, null=True, blank=True)
    wide_runs = models.IntegerField(default=0, null=True, blank=True)
    bye_runs = models.IntegerField(default=0, null=True, blank=True)
    legbye_runs = models.IntegerField(default=0, null=True, blank=True)
    noball_runs = models.IntegerField(default=0, null=True, blank=True)
    penalty_runs = models.IntegerField(default=0, null=True, blank=True)
    batsman_runs = models.IntegerField(default=0, null=True, blank=True)
    extra_runs = models.IntegerField(default=0, null=True, blank=True)
    total_runs = models.IntegerField(default=0, null=True, blank=True)
    player_dismissed = models.CharField(max_length=100, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=100, null=True, blank=True)
    fielder = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.match} - Over {self.over}.{self.ball}"
