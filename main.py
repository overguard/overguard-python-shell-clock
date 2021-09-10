from datetime import datetime as dt
import printer

def main():
    date_format = '%H:%M:%S'
    time = dt.strftime(dt.now(), date_format)

    printer.print_time(time)

if __name__ == '__main__':
    main()