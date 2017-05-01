class AppSettings(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from car_shop import settings
        getter = getattr(settings,
                         'SHOP_SETTING_GETTER',
                         lambda name, dflt: getattr(settings, name, dflt))
        return getter(self.prefix + name, dflt)

    @property
    def DEFAULT_SYMBOL(self):
        from car_shop import settings
        return self._setting("DEFAULT_SYMBOL",
                             getattr(settings, "DEFAULT_SYMBOL", '#'))

    @property
    def BANNER(self):
        from car_shop import settings
        return self._setting("BANNER",
                             getattr(settings, "BANNER", 'VEHICLE PRICE'))

    @property
    def HEADER(self):
        banner_length = len(list(self.BANNER)) + 10
        super_header = self.DEFAULT_SYMBOL * banner_length * 3
        first = self.DEFAULT_SYMBOL * banner_length
        middle = "%(f)s%(banner)s%(b)s" % dict(
            f=self.DEFAULT_SYMBOL * 5,
            banner=self.BANNER,
            b=self.DEFAULT_SYMBOL * 5
        )

        last = self.DEFAULT_SYMBOL * banner_length
        base_header = "%(first)s%(middle)s%(last)s" % dict(
            first=first,
            middle=middle,
            last=last)

        header = "%(super_header)s\n" \
                 "%(base_header)s\n" \
                 "%(super_header)s\n" % dict(super_header=super_header,
                                             base_header=base_header
                                             )
        return header

    @property
    def HEADER(self):
        banner_length = len(list(self.BANNER)) + 10
        super_header = self.DEFAULT_SYMBOL * banner_length * 3
        first = self.DEFAULT_SYMBOL * banner_length
        middle = "%(f)s%(banner)s%(b)s" % dict(
            f=self.DEFAULT_SYMBOL * 5,
            banner=self.BANNER,
            b=self.DEFAULT_SYMBOL * 5
        )

        last = self.DEFAULT_SYMBOL * banner_length
        base_header = "%(first)s%(middle)s%(last)s" % dict(
            first=first,
            middle=middle,
            last=last)

        header = "%(super_header)s\n" \
                 "%(base_header)s\n" \
                 "%(super_header)s\n" % dict(super_header=super_header,
                                             base_header=base_header
                                             )
        return header



import sys
app_settings = AppSettings('SHOP_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
