import requests

def get_and_save_phpsessid():
    smarthome_id = "id"
    smarthome_pw = "password"
    hostip = "0.0.0.0"
    
    try:
        # PHP 세션 ID 요청을 보내고 응답에서 추출
        url = f"http://{hostip}/webapp/data/getLoginWebApp.php?devce=WA&login_ide={smarthome_id}&login_pwd={smarthome_pw}"
        response = requests.get(url)
        response.raise_for_status()
        cookies = response.cookies
        phpsessid_cookie = cookies.get('PHPSESSID')

        if phpsessid_cookie is not None:
            with open('cookie_phpsessid', 'w') as file:
                file.write(phpsessid_cookie)
            return phpsessid_cookie
        else:
            return False, 'PHPSESSID 쿠키를 찾을 수 없습니다.'
    except requests.exceptions.RequestException as e:
        return False, f"HTTP 요청 중 오류 발생: {e}"
