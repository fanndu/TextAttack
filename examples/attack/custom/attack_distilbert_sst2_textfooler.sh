#!/bin/bash
# Shows how to attack your custom model using the TextFooler
# recipe and 10 examples.
textattack attack --model-from-file my_model.py --dataset-from-file my_model.py --recipe textfooler --num-examples 10