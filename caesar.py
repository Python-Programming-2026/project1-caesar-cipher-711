
"""
凯撒密码加密/解密工具

功能：
- 支持任意整数密钥（自动对26取模）
- 同时支持加密与解密
- 保留非字母字符（数字、符号、空格等）
- 可作为独立程序运行，也可作为模块导入
"""

from typing import List


def caesar(text: str, key: int, decrypt: bool = False) -> str:
    """
    凯撒密码核心函数

    参数：
    text : str
        需要处理的文本
    key : int
        密钥（任意整数）
    decrypt : bool
        是否为解密模式

    返回：
    str
        处理后的字符串
    """

    shift = key % 26
    if decrypt:
        shift = -shift

    result: List[str] = []

    for char in text:

        if char.isupper():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)

        elif char.islower():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)

        else:
            result.append(char)

    return ''.join(result)


def main():
    """交互式主程序"""

    print("=== 凯撒密码工具 ===")

    # 模式选择
    while True:
        mode = input("请选择模式：A=加密  B=解密：").strip().upper()
        if mode in ("A", "B"):
            break
        print("输入无效，请输入 A 或 B")

    # 密钥输入
    while True:
        try:
            key = int(input("请输入密钥（整数）："))
            break
        except ValueError:
            print("密钥必须是整数，请重新输入")

    # 文本输入
    if mode == "A":
        text = input("请输入明文：")
        result = caesar(text, key, decrypt=False)
        print("\n加密后的密文为：")
        print(result)

    else:
        text = input("请输入密文：")
        result = caesar(text, key, decrypt=True)
        print("\n解密后的明文为：")
        print(result)


if __name__ == "__main__":
    main()