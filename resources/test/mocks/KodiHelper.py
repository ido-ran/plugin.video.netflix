class KodiHelperMock(object):
    def __init__(self):
        self.log = lambda msg: None

    def get_base_data_path(self):
        return './_tmp/'
    