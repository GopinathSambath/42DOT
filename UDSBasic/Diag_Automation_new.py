# Import CANoe module
from py_canoe import CANoe
import configparser


def main():
    # create CANoe object

    cfg_file_path = parse_ini_file('Paths_diag.ini')
    print("CFG_FILE_PATH : ", cfg_file_path)
    canoe_inst = CANoe()

    # # open CANoe configuration. Replace canoe_cfg with yours.
    canoe_inst.open(canoe_cfg=cfg_file_path)
    #
    # # print installed CANoe application version
    canoe_inst.get_canoe_version_info()

    # Start CANoe measurement
    canoe_inst.start_measurement()

    # get signal value. Replace arguments with your message and signal data.
    goto_default_session = canoe_inst.send_diag_request('Door', "10 01")
    print("10 01 Response : ", goto_default_session)

    goto_io_session = canoe_inst.send_diag_request('Door', "2F 00 10 00")
    print("2F 00 10 Response : ", goto_io_session)

    dtc_cmd_1902 = canoe_inst.send_diag_request('Door', "19 02")
    print("19 02 Response : ", dtc_cmd_1902)

    # Stop CANoe Measurement
    canoe_inst.stop_measurement()

    # Quit / Close CANoe configuration
    canoe_inst.quit()


def parse_ini_file(file_path):
    config = configparser.ConfigParser()
    cfg_path = ""
    try:
        config.read(file_path)

        # Accessing the sections and their values
        path_section = config['PATHS']
        cfg_path = path_section.get('CFG_FILE_PATH')


    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except configparser.Error as e:
        print(f"Error parsing the INI file: {e}")

    return cfg_path


if __name__ == "__main__":
    main()

