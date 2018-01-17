#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

def gen_coupon(num=200):
    return [str(uuid.uuid4()) for __ in range(num)]
    
if __name__ == '__main__':
    with open('./result.txt', 'w') as file:
        coupons = gen_coupon()
        file.write('\n'.join(coupons))