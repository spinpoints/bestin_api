import requests

class LightControl:
    def __init__(self, hostip, id, phpsessid_value, user_name):
        self.smarthome_hostip = hostip
        self.smarthome_id = id
        self.smarthome_user_name = user_name
        self.phpsessid_value = phpsessid_value

    def control_light(self, room_num, unit_num, control_action):
        room_control_url = f"http://{self.smarthome_hostip}/webapp/data/getHomeDevice.php?req_name=remote_access_light&req_action=control&req_unit_num={unit_num}&req_ctrl_action={control_action}&req_dev_num={room_num}"
        room_control_headers = {
            "Cookie": f'PHPSESSID={self.phpsessid_value}; user_id={self.smarthome_id}; user_name={self.smarthome_user_name}',
        }

        response = requests.get(room_control_url, headers=room_control_headers)
        
        if response.status_code == 200:
            print("조명 제어 요청이 성공했습니다.")
            print(response)
        else:
            print("조명 제어 요청이 실패했습니다.")
            print("응답 코드:", response.status_code)
            print("응답 내용:", response.text)

# 설정 정보
smarthome_hostip = "hostip"
smarthome_id = "id"
phpsessid_value = 'cookie_phpsessid'

# 인스턴스 생성
light_controller = LightControl(smarthome_hostip, smarthome_id, phpsessid_value, "id")

# 조명 제어
room_num = "4"
unit_num = "1"
control_action = "off"
light_controller.control_light(room_num, unit_num, control_action)
