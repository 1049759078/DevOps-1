# -*- coding:utf-8 -*-
from execute.service import AnsibleService
from execute.callback import ResultCallback
from execute.models import Callback
from inventory.maker import Maker
__metaclass__ = type
class BasicAnsibleService(AnsibleService):
    def __init__(self,hostlist):
        self.maker = Maker()
        self.maker.inventory_maker(hostlist)
        super(BasicAnsibleService,self).__init__(self.maker.filename)

    def run(self,hostlist,tasklist):
        callback = ResultCallback()
        self.push_callback(callback)
        super(BasicAnsibleService,self).run(tasklist,self.maker)
        if callback.status == 1 :
            list = callback.ResultExtract()
            self.update(list,hostlist)
        else:
            for host in hostlist:
                host.status = callback.status
                host.save()

    def update(self,list,hostlist):
        for host in hostlist:
            host.coreness = list[0]
            host.memory = list[1]
            host.root_disk = list[2]
            host.hostname = list[3]
            host.status = 1
            host.save()