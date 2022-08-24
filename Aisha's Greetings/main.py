
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
    card = open(f'{card_type}.txt', 'r+')
    try:
      card.write(f'Dear {receiver}, \n')
      card.write(card.read())
      card.write(f' \n Sincerely, {sender}.')
      yield card

    finally:
      card.close()
'''
with generic('thankyou_card', 'Mwenda', 'Amanda') as card:
  print('Card Generated!')
  print(card.read())
'''
class personalized:
  def __init__(self, sender_name, receiver_name):
    self.sender_name = sender_name
    self.receiver_name = receiver_name
    self.file = open(f'{sender_name}_personalized.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear {self.receiver_name},')
    return self.file

  def __exit__(self, exc_type, exc_value, traceback):

    self.file.write(f'Sincerely {self.sender_name}.')
    self.file.close()

with personalized('John', 'Michael') as card:
  card.write(
  """
I am so proud of you! Being your friend for all these years has been nothing but a blessing. I do not say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.
  """
  )

with generic('happy_bday', 'Josiah', 'Remy') as bday_card:
  with personalized('Josiah', 'Esther') as personalized_card:
    personalized_card.write(
      """
      Happy Birthday!! I love you to the moon and back. Even though you are a pain sometimes, you are a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!
      """

    )

