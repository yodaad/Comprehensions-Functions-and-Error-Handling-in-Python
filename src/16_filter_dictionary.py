"""Filter function can also be used to filter dictionaries. In this example, we have a list of matches that contains dictionaries of football matches. 
We want to filter the matches where the home team won."""

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

# Filter the matches where the home team won and store them in a new list called home_winners using the filter function.
home_winners = list(filter(lambda item: item["home_team_result"] == "Win", matches))
print(home_winners)
print(len(home_winners))

# Filter the matches where the total number of goals scored is less than 3 and store them in a new list called less_goals using the filter function.
less_goals = list(filter(lambda goal: (goal["home_team_score"] + goal["away_team_score"]) < 3, matches))
print(less_goals)

