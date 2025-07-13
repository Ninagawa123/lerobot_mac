import glob
import time

def get_usb_serial_ports():
    """
    現在接続されているUSBシリアルデバイスのパス一覧を返す
    """
    tty_ports = glob.glob('/dev/tty.usb*')
    cu_ports = glob.glob('/dev/cu.usb*')
    # どちらでも使えるが、通常は tty.* の方が良い
    return sorted(set(tty_ports + cu_ports))

def find_new_usb_port(before, after):
    """
    2つのリストから、after にのみ存在するポート名（新規追加分）を返す
    """
    return list(set(after) - set(before))

if __name__ == '__main__':
    input("USBデバイスを抜いた状態でEnterキーを押してください...")
    ports_before = get_usb_serial_ports()
    print("抜いた状態のポート:", ports_before)

    input("USBデバイスを接続し、認識されてからEnterキーを押してください...")
    ports_after = get_usb_serial_ports()
    print("接続後のポート:", ports_after)

    new_ports = find_new_usb_port(ports_before, ports_after)
    if new_ports:
        print("新しく追加されたUSBポート名:")
        for port in new_ports:
            print(port)
    else:
        print("新しいUSBシリアルポートは見つかりませんでした。")
