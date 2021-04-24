from nba_api.stats.endpoints import teamgamelogs
import pandas as pd


def get_data():
    """
    Get game log data from nba_api (https://github.com/swar/nba_api).
    Save to csv.
    :return: None
    """

    # Make request to api
    game_logs = teamgamelogs.TeamGameLogs(season_nullable='2020-21').get_data_frames()
    df = pd.concat(game_logs)

    # Save response to csv
    df.to_csv('../data/season_game_logs.csv')


def load_df():
    """
    Load game logs from csv file.
    :return: Dataframe containing season game logs.
    """

    # Load data from csv file.
    return pd.read_csv('../data/season_game_logs.csv')


def filter_team_game_logs(df):
    """
    Create new dataframes for each team containing season game logs.
    Save each dataframe to a csv file within 'team_game_logs' directory.
        - File naming convention: ../data/team_game_logs/TEAM_ABBREVIATION_game_logs.csv
        - Example) ../data/team_game_logs/PHI_game_logs.csv
    :param df: Dataframe containing all game logs for all teams.
    :return: None
    """

    # Get list of all team ids.
    team_ids = df['TEAM_ID'].unique()

    # List of columns to keep from original dataframe.
    keep_columns = ['TEAM_ABBREVIATION', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA',
                    'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB',
                    'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']

    # Iterate over list of team ids.
    for i in team_ids:

        # Filter game logs for each team id.
        team_df = df[df['TEAM_ID'] == i]

        # Remove unnecessary columns.
        team_df = team_df.filter(keep_columns, axis=1)

        # Change index to represent game number.
        team_df.index = range(1, len(team_df) + 1)

        # Get team abbreviation.
        team_abbr = team_df['TEAM_ABBREVIATION'].unique()[0]

        # Format file name.
        team_csv = f'../data/team_game_logs/{team_abbr}_game_logs.csv'

        # Save to csv file.
        team_df.to_csv(team_csv)


def main():
    df = load_df()
    filter_team_game_logs(df)


if __name__ == '__main__':
    main()
