#!/usr/bin/python3
def magic_string(m_s=[0]):
    m_s += 1
    return (str("BestSchool, " * (m_s[0] - 1)) + "BestSchool")
