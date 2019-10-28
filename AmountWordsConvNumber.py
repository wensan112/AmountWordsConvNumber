# -*- coding:utf-8 -*-

import re

class AmountWordsConvNumber:
    
    def __init__(self):
        self.__words_num = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖', '0': '零'}
        self.__rmb_unit = '仟佰拾亿仟佰拾万仟佰拾元角分'
        self.__dic_rule = {'零角零分$': '整', '零[仟佰拾]': '零', '零{2,}': '零', '零([亿|万])': '$1', '零+元': '元', '亿零{0,3}万': '亿', '^元': '零元'}

    def validity_Chinese(self):
        '''
        unicode 分配给汉字（中日韩越统一表意文字）的范围为 4E00-9FFFpass
        '''
        return all('\u4e00' <= char <= '\u9fff' for char in self.__text)

    def validity_number(self, number):
        number_list = number.split('.')
        for str in number_list:
            if re.match('[0-9]{1,}', str) is None:
                return False
        return True

    def words_conv_number(self, words):
        pass

    def number_conv_words(self, number):
        '''
        1.小写金额转化为大写金额
        2.小写金额精确到两位以下
        '''
        #数字字符串处理
        number_list = number.split('.')
        if len(number_list) == 1:
            number = number + '00'
        elif len(number_list) == 2 and len(number_list[1]) == 2:
            number = number_list[0] + number_list[1]
        elif len(number_list) == 2 and len(number_list[1]) == 1:
            number = number_list[0] + number_list[1] + '0'
        else:
            return False

        #单位和数字字符串相对应截取
        unit = self.__rmb_unit[len(self.__rmb_unit) - len(number) :]

        index, strout = 0,''
        for key in number:
            strout = strout +  self.__words_num[key] + unit[index]
            index = index + 1

        for keys in self.__dic_rule.keys():
            rule = re.compile(keys)
            strout = rule.sub(self.__dic_rule[keys], strout)

        return strout
