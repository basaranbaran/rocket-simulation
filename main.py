from rocket_lib import RocketLandingPlatform


def main():
    print("Valde Roket İniş Simülasyonu")

    try:
        platform = RocketLandingPlatform(
            platform_x=5,
            platform_y=5,
            width=5,
            height=5,
            area_width=24,
            area_height=32
        )

        print(
            f"Platform başarıyla kuruldu: [{platform.platform_x},{platform.platform_y}] noktasında {platform.width}x{platform.height} boyutunda.")

        print(f"Genel Alan Sınırları: {platform.area_width}x{platform.area_height}")

    except ValueError as e:
        print(e)
        return

    print("\nİniş Talepleri:")

    print(f"Roket (5, 5)   -> {platform.request_landing(5, 5)}")

    print(f"Roket (11, 10) -> {platform.request_landing(11, 10)}")

    print(f"Roket (5, 5)   -> {platform.request_landing(5, 5)}")

    print(f"Roket (6, 6)   -> {platform.request_landing(6, 6)}")

    print(f"Roket (7, 7)   -> {platform.request_landing(7, 7)}")

    print(f"Roket (30, 20) -> {platform.request_landing(30, -20)}")


if __name__ == "__main__":
    main()