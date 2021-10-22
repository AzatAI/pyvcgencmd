# python core imports
import subprocess
import shlex
import re
from typing import Dict, List
from datetime import datetime

# to check space and memory
from utils import check_disk_usage
import psutil

# pydantic imports
from pydantic import BaseModel

"""TODO

camera          get_camera
state           get_throttled
temperature     measure_temp
arm_clock       measure_clock arm
core_clock      measure_clock core
serial_clock    measure_clock uart
storage_clock   measure_clock emmc
voltage         measure_volts
otp             otp_dump
cpu_memory      get_mem arm
gpu_memory      get_mem gpu
config          get_config [config|int|str]
---------------------------------------
space
memory

"""


class Camera(BaseModel):
    supported: int
    detected: int


class State(BaseModel):
    throttled: bytes


class Temperature(BaseModel):
    temperature: float


class ArmClock(BaseModel):
    arm_clock: int


class CoreClock(BaseModel):
    core_clock: int


class SerialClock(BaseModel):
    serial_clock: int


class StorageClock(BaseModel):
    storage_clock: int


class Voltage(BaseModel):
    voltage: float


class Otp(BaseModel):
    otp: Dict[str, bytes]


class CpuMemory(BaseModel):
    cpu_memory: int


class GpuMemory(BaseModel):
    gpu_memory: int


class Config(BaseModel):
    config: Dict[str, bytes]


class Space(BaseModel):
    total: int
    used: int
    unused: int


class Memory(BaseModel):
    total: int
    available: int
    percent: float
    used: int
    free: int


class Vcmd:
    # supported cmds
    cmds: List = [
        "get_camera",
        "get_throttled",
        "measure_temp",
        "measure_clock arm",
        "measure_clock core",
        "measure_clock uart",
        "measure_clock emmc",
        "measure_volts",
        "otp_dump",
        "get_mem arm",
        "get_mem gpu",
        "get_config int",
    ]
    extra_cmds: List = ["space", "memory"]
    data_format: str
    describe: bool
    # cmd values
    updated: datetime
    camera: Camera
    state: State
    temperature: Temperature
    arm_clock: int
    core_clock: int
    serial_clock: int
    storage_clock: int
    voltage: float
    otp: dict
    cpu_memory: int
    gpu_memory: int
    config: dict
    space: dict
    memory: str

    def __init__(self, data_fromat: str = "numeric", describe: bool = False) -> None:
        self.data_format = data_fromat
        self.describe = describe
        # update readings
        self.updated = datetime.utcnow()
        # update camera
        self.camera = Camera(
            **{
                key: (self.__camera())[i]
                for i, key in enumerate(Camera.__fields__.keys())
            }
        )
        # update state
        val = self.__state()
        self.state = State(
            **{key: val for i, key in enumerate(State.__fields__.keys())}
        )
        # update temperature
        val = self.__temperature()
        self.temperature = Temperature(
            **{key: val for i, key in enumerate(Temperature.__fields__.keys())}
        )
        # arm_clock

    def __run_cmd(self, cmd):
        args = shlex.split(cmd)
        args.insert(0, "vcgencmd")
        out = (
            subprocess.check_output(args, stderr=subprocess.PIPE)
            .decode("utf-8")
            .strip()
        )
        return out

    def __camera(self):
        cmd = "get_camera"
        out = self.__run_cmd(cmd)
        out = out.split(" ")
        out = list(filter(None, out))
        out = [int(each.split("=")[1]) for each in out]
        return out

    def __state(self):
        cmd = "get_throttled"
        out = self.__run_cmd(cmd)
        out = out.split("=")[1]
        return out

    def __temperature(self):
        cmd = "measure_temp"
        out = self.__run_cmd(cmd)
        out = out.split("=")[1].split("'")[0]
        return out

    def __arm_clock(self):
        cmd = "measure_clock arm"
        out = self.__run_cmd(cmd)
        return out

    def __core_clock(self):
        cmd = "measure_clock core"
        out = self.__run_cmd(cmd)
        return out

    def __serial_clock(self):
        cmd = "measure_clock uart"
        out = self.__run_cmd(cmd)
        return out

    def __storage_clock(self):
        cmd = "measure_clock emmc"
        out = self.__run_cmd(cmd)
        return out

    def __voltage(self):
        cmd = "measure_volts"
        out = self.__run_cmd(cmd)
        return out

    def __otp(self):
        cmd = "measure_volts"
        out = self.__run_cmd(cmd)
        return out


vcmd = Vcmd()
print(vcmd.state)
