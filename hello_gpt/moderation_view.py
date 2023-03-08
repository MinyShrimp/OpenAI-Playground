class ModerationView:
    """
    Since: 2023-03-09
    Author: 김회민 ksk7584@gmail.com
    """

    @staticmethod
    def view(inputs: list[str], response: dict):
        results = response["results"]

        print("======= Moderation Result =======")
        print("Model Name: [{}]".format(response["model"]))
        for _input, result in zip(inputs, results):
            categories = result["categories"]

            print("\n= [{}]".format(_input))
            print("Result: {}".format(result["flagged"]))
            print("== Categories")
            print(
                "hate:\t{}\thate/threatening:\t{}\tself-harm:\t{}"
                .format(categories["hate"], categories["hate/threatening"], categories["self-harm"])
            )
            print(
                "sexual:\t{}\tsexual/minors:\t\t{}\tviolence:\t{}\tviolence/graphic: {}"
                .format(
                    categories["sexual"], categories["sexual/minors"],
                    categories["violence"], categories["violence/graphic"]
                )
            )
