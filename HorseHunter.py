import random
import time
import argparse
import time
import signal
import sys
import os


import pyperclip

from replaceF2M import replaceF2M

global targetDict
global levelDict
global startTime
global outputLinesCount


targetDict = {
    "female": "令堂",
    "male": "令尊",
    "mix": "混合",
}

levelDict = {
    "max": "火力全开",
    "min": "口吐芬芳",
    "mix": "混合",
}


def signal_handler(signal, frame):
    endTime = time.time()
    print(f"本次使用时间：{round(endTime-startTime, 1)}s")
    print(f"共问候对面：{outputLinesCount} 次")
    sys.exit(0)


def parseArgs():
    def helpDict(d):
        return ", ".join([
            k+"="+d[k] for k in d
        ])
    parser = argparse.ArgumentParser(description='自动向剪贴板刷新金句，让你不再饱受欺凌')

    parser.add_argument('--target', '-t', dest='target',  choices=["female", "male", "mix"], default="female",
                        help='设置辱骂对象, '+helpDict(targetDict)+'. 默认 female')
    parser.add_argument('--level', '-l', dest='level',  choices=["max", "min", "mix"], default="max",
                        help='设置辱骂等级, '+helpDict(levelDict)+'. 默认 max')
    parser.add_argument('--interval', '-i', dest='interval', type=float, default=0.1,
                        help='设置刷新间隔(s). 默认 0.1')

    args = parser.parse_args()

    if args.interval < 0:
        raise argparse.ArgumentTypeError("assert: INTERVAL >= 0")

    config = {}
    config["target"] = args.target
    config["level"] = args.level
    config["interval"] = args.interval

    return config


def getLines(config):

    linesFemale = []
    linesMale = []

    if config['level'] == "max" or config['level'] == "mix":
        with open("resources-max.txt", "r", encoding="utf-8") as resources:
            linesFemale += resources.readlines()

    if config['level'] == "min" or config['level'] == "mix":
        with open("resources-min.txt", "r", encoding="utf-8") as resources:
            linesFemale += resources.readlines()

    if config['target'] == "female":
        return linesFemale
    else:
        linesMale = [replaceF2M(s) for s in linesFemale]

        if config['target'] == "male":
            return linesMale
        else:
            return linesFemale + linesMale


if __name__ == "__main__":
    path = getattr(sys, '_MEIPASS', os.getcwd())
    os.chdir(path)

    print("本软件仅限用于自卫反击，向网络暴力说不！！")

    config = parseArgs()

    lines = getLines(config)

    print("辱骂对象：" + targetDict[config["target"]])
    print("辱骂等级：" + levelDict[config["level"]])
    print(f"候选金句：{len(lines)}")
    print(f"刷新间隔：{config['interval']}s")

    startTime = time.time()
    outputLinesCount = 0
    signal.signal(signal.SIGINT, signal_handler)

    print("持续输出中...")
    while True:
        outputLinesCount += 1
        pyperclip.copy(random.choice(lines))
        time.sleep(config["interval"])
