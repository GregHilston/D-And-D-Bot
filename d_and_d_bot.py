import random
from simple_slack_bot.simple_slack_bot import SimpleSlackBot

simple_slack_bot = SimpleSlackBot(debug=True)


@simple_slack_bot.register("message")
def roll_callback(request):
    """This function is called every time a message is sent to a channel out Bot is in

    :param request: the SlackRequest we receive along with the event. See the README.md for full documentation
    :return: None
    """
    if request.message.lower().startswith("roll"):
        dice_num_and_value = request.message.lower().split("roll")[1]

        try:
            dice_num = int(dice_num_and_value.split("d")[0])
            dice_value = int(dice_num_and_value.split("d")[1])
        except ValueError:
            request.write("Invalid format detected. Please call this bot using roll [int]d[int]")
            return


        sum = 0
        rolls = []

        if dice_num > 25:
            request.write("We will not process more than 25 dice rolls, sorry @who_dat")
            return

        for die in range(dice_num):
            roll = random.randint(1, dice_value)
            sum += roll
            rolls.append(roll)

        request.write(f"Rolled {dice_num_and_value} and got {str(sum)} ({rolls})")


def main():
    simple_slack_bot.start()


if __name__ == "__main__":
    main()
