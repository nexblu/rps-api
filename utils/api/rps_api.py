import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse


class RpsAPI:
    def __init__(self) -> None:
        self.choice = ['rock', 'paper', 'scissors']

    def vs_bot(self, choice: str) -> JSONResponse:
        computer_choice = random.choice(self.choice)
        choice = choice.lower()
        print(choice)
        if choice in self.choice:
            if choice == computer_choice:
                status = 'it\'s a tie!'
            elif (choice == 'rock' and computer_choice == 'scissors') or \
                (choice == 'paper' and computer_choice == 'rock') or \
                    (choice == 'scissors' and computer_choice == 'paper'):
                status = 'you win'
            else:
                status = 'you lose'
            return JSONResponse(
                content=[
                    {
                        'ditttt-rps': {
                            'result': {
                                'you choice': choice,
                                'bot choice': computer_choice,
                                'status': status
                            },
                            'status_code': 200
                        }
                    }
                ],
                status_code=200
            )
        else:
            return JSONResponse(
                content=[
                    {
                        'ditttt-rps': {
                            'result': 'invalid input',
                            'status_code': 400
                        }
                    }
                ],
                status_code=400
            )

    def get_random(self, amount: str) -> JSONResponse:
        try:
            amount = int(amount)
        except:
            return JSONResponse(
                content=[
                    {
                        'ditttt-rps': {
                            'result': f'{amount} is not number',
                            'status_code': 400
                        }
                    }
                ],
                status_code=400
            )
        else:
            if amount > 5:
                return JSONResponse(
                    content=[
                        {
                            'ditttt-rps': {
                                'result': f'The number must not exceed 5',
                                'status_code': 400
                            }
                        }
                    ],
                    status_code=400
                )
            elif amount <= 0:
                return JSONResponse(
                    content=[
                        {
                            'ditttt-rps': {
                                'result': f'The number must must be 1 - 5',
                                'status_code': 400
                            }
                        }
                    ],
                    status_code=400
                )
            else:
                return JSONResponse(
                    content=[
                        {
                            'ditttt-rps': {
                                'result': random.choices(self.choice, k=amount),
                                'status_code': 200
                            }
                        }
                    ],
                    status_code=200
                )
