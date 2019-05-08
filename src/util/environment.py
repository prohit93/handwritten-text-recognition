"""Set paths and environment variables"""

import os


class Env():

    def __init__(self, args):
        self.raw_source = os.path.join("..", "raw", args.dataset)
        self.source = os.path.join("..", "data", args.dataset)
        self.output = os.path.join("..", "output", args.dataset)
        self.output_tasks = os.path.join(self.output, "tasks")

        self.train = os.path.join(self.source, "train.npz")
        self.valid = os.path.join(self.source, "valid.npz")
        self.test = os.path.join(self.source, "test.npz")

        self.epochs = args.epochs
        self.batch_size = args.batch_size

        self.model_input_size = (800, 64, 1)
        self.max_text_length = 128