#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 核心类
# 用于读取YAML和JSON格式的文件
from ansible.parsing.dataloader import DataLoader

# 用于导入资产文件
from ansible.inventory.manager import InventoryManager
# 用于存储各类变量信息
from ansible.vars.manager import VariableManager

# 操作单个主机信息
from ansible.inventory.host import Host
# 操作单个主机组信息
from ansible.inventory.group import Group
# 存储执行hosts的角色信息
from ansible.playbook.play import Play
# ansible底层用到的任务队列
from ansible.executor.task_queue_manager import TaskQueueManager
# 核心类执行playbook
from ansible.executor.playbook_executor import PlaybookExecutor


def  adhoc():
    """
    ad-hoc 调用

    """

    # 资产配置信息
    dl = 'aa'