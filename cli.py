import random
import argparse
from game import Game


def generate_unique_3digit_number() -> str():
    digits = random.sample(range(10), 3)  # 중복 없이 3개 숫자 선택
    return str(digits[0] * 100 + digits[1] * 10 + digits[2])


def main():
    parser = argparse.ArgumentParser(description="Baseball game CLI")
    parser.add_argument("--user", required=False, help="사용자 이름")
    args = parser.parse_args()
    game = Game()
    question = generate_unique_3digit_number()
    game.question = question

    print(f"안녕하세요, {args.user}님! Baseball game을 시작합니다.\n")
    # print(f"정답은 {game._question}")

    while True:
        command = input("정답을 입력해 주세요.(세 자리 수를 입력): ").strip()
        if command == "exit":
            print("종료합니다.")
            break
        try:
            game_result = game.guess(command)
            print(f"결과: {game_result.solved}")
            print(f"스트라이크: {game_result.strikes}")
            print(f"볼: {game_result.balls}")
            if game_result.solved:
                print("정답을 맞추셨습니다. 축하합니다!")
                break

        except TypeError as e:
            print(f"잘못된 입력값입니다: ({str(e)})")


if __name__ == "__main__":
    main()
