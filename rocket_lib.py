class RocketLandingPlatform:
    def __init__(self, platform_x, platform_y, width, height, area_width=None, area_height=None):

        self.platform_x = platform_x
        self.platform_y = platform_y
        self.width = width
        self.height = height
        self.area_width = area_width
        self.area_height = area_height

        if self.area_width is not None and self.area_height is not None:
            if (platform_x + width > area_width) or (platform_y + height > area_height):
                raise ValueError("Hata: Platform, tanımlanan genel alanın dışına taşıyor!")
        self.landed_rockets = []

    def request_landing(self, x, y):

        if self.area_width is not None and self.area_height is not None:
            if not (0 <= x < self.area_width and 0 <= y < self.area_height):
                return "Genel harita dışı"

        if self.area_width is not None:
            if not (0 <= x < self.area_width and 0 <= y < self.area_height):
                return "Platform dışı"

        if not (self.platform_x <= x < self.platform_x + self.width):
            return "Platform dışı"

        if not (self.platform_y <= y < self.platform_y + self.height):
            return "Platform dışı"

        for existing_x, existing_y in self.landed_rockets:
            if self._is_neighbor(x, y, existing_x, existing_y):
                return "Çarpışma"

        self.landed_rockets.append((x, y))
        return "İniş için uygun"

    def _is_neighbor(self, x1, y1, x2, y2):
        diff_x = abs(x1 - x2)
        diff_y = abs(y1 - y2)

        return diff_x <= 1 and diff_y <= 1