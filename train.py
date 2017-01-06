from src.dataset.datagenerator import *  
from src.model.sketch_to_code import *
import os
from argparse import ArgumentParser
VAL_SPLIT = 0.2
MAX_SEQ = 150
EPOCHS = 1




def main():
    parser = build_parser()
    options = parser.parse_args()
    data_input_path = input("Enter full path to dataset: ")
    validation_split = input("Enter portion of training data to be used as validation dataset: ")
    epochs = input("number of epochs to train on: ")
    model_output_path = input("Enter full path for saving model data")
    vocab_path = input("Enter full path for words set")

    if not os.path.exists(model_output_path):
        os.makedirs(model_output_path)


    sketchtocode = sketch_to_code(model_output_path,data_input_path,vocab_path)
    model = sketchtocode.create_model()

    print("Created new model")

    sketchtocode.train(model,data_input_path,validation_split,epochs)

    print("Model_training_complete and saved at {}".format(model_output_path))


if __name__ == "__main__":
    main()

