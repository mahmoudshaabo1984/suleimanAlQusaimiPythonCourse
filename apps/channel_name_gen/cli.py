import argparse
from .generator import generate_batch


def main() -> None:
    parser = argparse.ArgumentParser(description="Channel name generator")
    parser.add_argument("-n", "--count", type=int, default=10, help="عدد الأسماء المطلوبة")
    parser.add_argument("-l", "--lang", choices=["ar", "en"], default="ar", help="لغة الكلمات")
    parser.add_argument(
        "-s",
        "--style",
        choices=["kebab", "snake", "camel", "plain"],
        default="kebab",
        help="تنسيق الاسم",
    )
    parser.add_argument("--number", action="store_true", help="إلحاق رقم عشوائي")
    args = parser.parse_args()

    names = generate_batch(
        count=args.count, lang=args.lang, style=args.style, include_number=args.number
    )
    for x in names:
        print(x)


if __name__ == "__main__":
    main()

