# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/8/22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import multiprocessing as mp
import queue
from download_data import download_data


def run(data, mp_name):
    print('开始进程:【' + mp_name + "】")
    # print(data)
    download_data.save_data(data)


if __name__ == '__main__':
    # 登录淘宝联盟
    download_data.login()
    # coupon_list = download_data.read_excel('./excel/2019-08-27_导出优惠券.xls')
    # if len(coupon_list) > 1000:
        # coupon_list_data = [coupon_list[i:i + 1000] for i in range(0, len(coupon_list), 1000)]
        # #print(len(coupon_list_data)
        # mp_list = []
        # for i in range(0, len(coupon_list_data)):
        #     mp_name = mp.Process(target=run, args=(coupon_list_data[i], 'mp_name_' + str(i)))
        #     mp_list.append(mp_name)
        # print(mp_list)
        # if len(mp_list) > 0:
        #     for item in mp_list:
        #         item.start()
        #     for item_stop in mp_list:
        #         item_stop.join()
