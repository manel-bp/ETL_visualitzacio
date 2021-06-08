import pandas as pd

# Load data into Dataframes
states = pd.read_csv('dataset/States.csv')
df_2 = pd.read_csv('dataset/Basic_Stats.csv')

# Get the state of birth code
df_2['state_of_birth'] = df_2['Birth Place'].str[-2:]

# Join to a dictionary to get the state name
df_with_states = pd.merge(df_2, states[['State', 'Code']], left_on="state_of_birth", right_on="Code", how="left")

# Get the number of years played
df_with_states['first_year_played'] = df_with_states['Years Played'].str[0:4]
df_with_states['last_year_played'] = df_with_states['Years Played'].str[-4:]
df_with_states.loc[df_with_states['first_year_played'].notnull(), 'first_year_played'] = df_with_states.loc[df_with_states['first_year_played'].notnull(), 'first_year_played'].apply(int)
df_with_states.loc[df_with_states['last_year_played'].notnull(), 'last_year_played'] = df_with_states.loc[df_with_states['last_year_played'].notnull(), 'last_year_played'].apply(int)
df_with_states['num_years_played'] = df_with_states['last_year_played'] - df_with_states['first_year_played'] + 1

# Create a csv file to read in Tableau with the applied ETL
df_with_states.to_csv('dataset/Basic_Stats_2.csv')

