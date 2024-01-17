import os
'''
import pytorch_lightning as pl
from meter.config import ex
from meter.modules import METERTransformerSS
from meter.datamodules.multitask_datamodule import MTDataModule
'''

def get_input():
    # read question and question from cache
    qf = open("cache/input.txt")
    question = qf.read()
    qf.close()
    image = "cache/input.jpg"
    try:
        os.remove("cache/output.txt") # signal of answer existing
    except:
        pass
    return image, question

def output(answer):
    # write answer to cache
    af = open("cache/output.txt", "w")
    af.write(answer)
    af.close()

def predict(image, question):
    # Finish this function
    '''
    model = METERTransformerSS(_config) # load model
    # how to get answer from model (image, question)
    model.single_inference(image, question)
    '''
    answer = "Here are many students in a park with a flag"
    return answer

def main():
    image, question = get_input()
    answer = predict(image, question)
    output(answer)

if __name__ == "__main__":
    main()
    