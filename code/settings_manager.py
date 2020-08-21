import uos, ujson


class SettingsManager(object):
    def __init__(self):
        self.settings_path = "/sd/settings.config"
        self.face_reg = 1
        self.mask_det = 1
        self.hot_map = 1
        # "KR", "EN"
        self.language = "KR"
        self.passwd = "0000"

    def set_face_reg(self, value:int):
        self.face_reg = value

    def set_mask_det(self, value:int):
        self.mask_det = value

    def set_hot_map(self, value:int):
        self.hot_map = value

    def set_language(self, value:str):
        self.set_language = value

    def set_passwd(self, value:str):
        self.passwd = value

    def read_settings(self):
        try:
            return ujson.load(open(self.settings_path, "r"))
        except Exception:
            return self.__dict__

    def write_settings(self):
        ujson.dump(self.__dict__, open(self.settings_path, 'w+'))


if __name__ == "__main__":
    sm = SettingsManager()
    res = sm.read_settings()
    print(res)

    sm.hot_map = 0
    sm.write_settings()

    res = sm.read_settings()
    print(res)
