import click
from helpers.FileProcessor import FileProcessor
from configs import config


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def main(files: list) -> bool:
    config.logger.info(f'Files processing...')
    df_processor = FileProcessor(files=files)
    result = df_processor.df_processing()

    config.logger.info('Results:')
    for rows in result:
        config.logger.info(f"{rows['file_name']}: {rows['Timestamp']}, {rows['Full_name']}, {rows['Passport_number']}, {rows['Flight_ticket']}")
    return True


if __name__ == "__main__":
    main()
