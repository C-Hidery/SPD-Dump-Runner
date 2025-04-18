#SPD Dump Runner Version 1.3.1 By Ryan Crepa
import asyncio
import configparser
import os
file_path = "config.ini"
config = configparser.ConfigParser()
if os.path.exists(file_path):
    config.read('config.ini')
    sprd4 = config.get('SDR-config', 'sprd4')
    reatt = config.get('SDR-config', 'reattach')
    blk = config.getint('SDR-config', 'blk_size')
    fdl_use = config.get('SDR-config' , 'use_custom_fdl')
    fdl_1_c = config.get('SDR-config', 'FDL1_file_addr')
    fdl_1_addr = config.get('SDR-config', 'FDL1_to_addr')
    fdl_2_c = config.get('SDR-config', 'FDL2_file_addr')
    fdl_2_addr = config.get('SDR-config','FDL2_to_addr')
    tout = config.get('SDR-config', 'timeout')
else:
    print("\n创建配置文件......\n")
    os.system("echo [SDR-config] >> config.ini")
    os.system("echo sprd4 = no >> config.ini")
    os.system("echo reattach = no >> config.ini")
    os.system("echo blk_size = 50000 >> config.ini")
    os.system("echo use_custom_fdl = no >> config.ini")
    os.system("echo FDL1_file_addr = >> config.ini")
    os.system("echo FDL1_to_addr = 0x5000 >> config.ini")
    os.system("echo FDL2_file_addr = >> config.ini")
    os.system("echo FDL2_to_addr = 0x9efffe00 >> config.ini")
    os.system("echo timeout = 30 >> config.ini")
    config.read('config.ini')
    sprd4 = config.get('SDR-config', 'sprd4')
    reatt = config.get('SDR-config', 'reattach')
    blk = config.getint('SDR-config', 'blk_size')
    fdl_use = config.get('SDR-config' , 'use_custom_fdl')
    fdl_1_c = config.get('SDR-config', 'FDL1_file_addr')
    fdl_1_addr = config.get('SDR-config', 'FDL1_to_addr')
    fdl_2_c = config.get('SDR-config', 'FDL2_file_addr')
    fdl_2_addr = config.get('SDR-config','FDL2_to_addr')
    tout = config.get('SDR-config', 'timeout')
class CMDController:
    def __init__(self):
        self.proc = None
        self.running = True
        # 带交互的快捷命令配置
        self.command_handlers = {
            'boot': self._handle_boot_device,
            'boot-fdl': self._handle_boot_fdl_device,
            'boot-c': self._handle_boot_config,
            'q': self._handle_exit,
            'w': self._handle_write,
            'r': self._handle_read,
            'e': self._handle_erase,
            'config': self._handle_config
        }

    async def async_input(self, prompt):
        """异步获取用户输入"""
        return await asyncio.get_event_loop().run_in_executor(
            None, input, prompt
        )
    async def _handle_exit(self):
        return "exit"
    async def _handle_config(self):
        config.read('config.ini')
        sprd4 = config.get('SDR-config', 'sprd4')
        reatt = config.get('SDR-config', 'reattach')
        blk = config.getint('SDR-config', 'blk_size')
        fdl_use = config.get('SDR-config' , 'use_custom_fdl')
        fdl_1_c = config.get('SDR-config', 'FDL1_file_addr')
        fdl_1_addr = config.get('SDR-config', 'FDL1_to_addr')
        fdl_2_c = config.get('SDR-config', 'FDL2_file_addr')
        fdl_2_addr = config.get('SDR-config','FDL2_to_addr')
        tout = config.get('SDR-config', 'timeout')
        print("配置文件信息：")
        print(f"1. 是否使用SPRD4 = {sprd4}")
        print(f"2. 是否重连 = {reatt}")
        print(f"3. blk_size大小 = {blk}")
        print(f"4. 是否使用自定义FDL = {fdl_use}")
        print(f"5. FDL1文件地址 = {fdl_1_c}")
        print(f"6. FDL1欲发送地址 = {fdl_1_addr}")
        print(f"7. FDL2文件地址 = {fdl_2_c}")
        print(f"8. FDL2欲发送地址 = {fdl_2_addr}")
        print(f"9. 超时时间 = {tout}")
        set1 = input("输入欲修改值的序号：")
        if set1 == '1':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4': f"{set2}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '2':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{set2}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '3':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{set2}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '4':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{set2}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '5':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{set2}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '6':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{set2}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '7':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{set2}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '8':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{set2}",
                'timeout' : f"{tout}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        elif set1 == '9':
            set2 = input("请输入值：")
            config['SDR-config'] = {
                'sprd4' : f"{sprd4}",
                'reattach': f"{reatt}",
                'blk_size' : f"{blk}",
                'use_custom_fdl' : f"{fdl_use}",
                'FDL1_file_addr' : f"{fdl_1_c}",
                'FDL1_to_addr': f"{fdl_1_addr}",
                'FDL2_file_addr': f"{fdl_2_c}",
                'FDL2_to_addr' : f"{fdl_2_addr}",
                'timeout' : f"{set2}"
            }
            with open('config.ini', 'w') as f:
                config.write(f)
        else:
            print("Bad value!")
        config.read('config.ini')
        sprd4 = config.get('SDR-config', 'sprd4')
        reatt = config.get('SDR-config', 'reattach')
        blk = config.getint('SDR-config', 'blk_size')
        fdl_use = config.get('SDR-config' , 'use_custom_fdl')
        fdl_1_c = config.get('SDR-config', 'FDL1_file_addr')
        fdl_1_addr = config.get('SDR-config', 'FDL1_to_addr')
        fdl_2_c = config.get('SDR-config', 'FDL2_file_addr')
        fdl_2_addr = config.get('SDR-config','FDL2_to_addr')
        return ""
    async def _handle_boot_config(self):
        config.read('config.ini')
        sprd4 = config.get('SDR-config', 'sprd4')
        reatt = config.get('SDR-config', 'reattach')
        blk = config.getint('SDR-config', 'blk_size')
        fdl_use = config.get('SDR-config' , 'use_custom_fdl')
        fdl_1_c = config.get('SDR-config', 'FDL1_file_addr')
        fdl_1_addr = config.get('SDR-config', 'FDL1_to_addr')
        fdl_2_c = config.get('SDR-config', 'FDL2_file_addr')
        fdl_2_addr = config.get('SDR-config','FDL2_to_addr')
        tout = config.get('SDR-config', 'timeout')
        if sprd4 == 'yes':
            if fdl_use == 'yes':
                return f"dump.exe --kickto 2 --wait {tout} fdl {fdl_1_c} {fdl_1_addr} fdl {fdl_2_c} {fdl_2_addr} exec blk_size {blk}"
            else:
                return f"dump.exe --kickto 2 --wait {tout} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec blk_size {blk}"
        else:
            if fdl_use == 'yes':
                if reatt == 'yes':
                    return f"dump.exe -r --wait {tout} fdl {fdl_1_c} {fdl_1_addr} fdl {fdl_2_c} {fdl_2_addr} exec blk_size {blk}"
                else:
                    return f"dump.exe --wait {tout} fdl {fdl_1_c} {fdl_1_addr} fdl {fdl_2_c} {fdl_2_addr} exec blk_size {blk}"
            else:
                if reatt == 'yes':
                    return f"dump.exe -r --wait {tout} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec blk_size {blk}"
                else:
                    return f"dump.exe --wait {tout} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec blk_size {blk}"
    async def _handle_write(self):
        part = await self.async_input("输入欲操作分区：")
        adr = await self.async_input("输入镜像文件路径：")
        return f"w {part} {adr}"
    async def _handle_read(self):
        part = await self.async_input("输入欲操作分区：")
        return f"r {part}"
    async def _handle_erase(self):
        part = await self.async_input("输入欲操作分区：")
        return f"e {part}"
    async def _handle_boot_device(self):
        kick = await self.async_input("是否需要使用SPRD4？（可能会擦除Splloader） (Y/n)")
        if kick == 'y':
            timeout = await self.async_input("输入超时时间：（默认为300s）")
            return f"dump.exe --kickto 2 --wait {timeout or '300'} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec"
        elif kick == 'n':
            reattach = await self.async_input("是否使用重连？（SPRD4不支持）（Y/n）")
            if reattach == 'y':
                timeout = await self.async_input("输入超时时间：（默认为30s）：")
                return f"dump.exe -r --wait {timeout or '30'} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec"
            elif reattach == 'n':
                timeout = await self.async_input("输入超时时间：（默认为30s）：")
                return f"dump.exe --wait {timeout or '30'} loadfdl 0x5000.bin loadfdl 0x9efffe00.bin exec"
            
        #return f"dir /s {path or '.'} {file_type or '*.*'}"
    
    async def _handle_boot_fdl_device(self):
        cus = await self.async_input("是否使用本地FDL模式？（可以在本地目录内读取“FDL1-custom.img”和“FDL2-custom.img”分别用于FDL1/2，使用时请将自定义FDL重命名！）（Y/n）")
        if cus == 'y':
            fdl_1_adr = await self.async_input("输入fdl1载入地址（默认为0x5000）:")
            fdl_2_adr = await self.async_input("输入fdl2载入地址（默认为0x9efffe00）:")
            kick = await self.async_input("是否需要使用SPRD4？（可能会擦除Splloader） (Y/n)")
            if kick == 'y':
                timeout = await self.async_input("输入超时时间：（默认为300s）")
                return f"dump.exe --kickto 2 --wait {timeout or '300'} fdl  FDL1-custom.img {fdl_1_adr or '0x5000'} fdl FDL2-custom.img {fdl_2_adr or '0x9efffe00'} exec"
            elif kick == 'n':
                reattach = await self.async_input("是否使用重连？（SPRD4不支持）（Y/n）")
                if reattach == 'y':
                    timeout = await self.async_input("输入超时时间：（默认为30s）：")
                    return f"dump.exe -r --wait {timeout or '30'} fdl FDL1-custom.img {fdl_1_adr or '0x5000'} fdl FDL2-custom.img {fdl_2_adr or '0x9efffe00'} exec"
                elif reattach == 'n':
                    timeout = await self.async_input("输入超时时间：（默认为30s）：")
                    return f"dump.exe --wait {timeout or '30'} fdl FDL1-custom.img {fdl_1_adr or '0x5000'} fdl FDL2-custom.img {fdl_2_adr or '0x9efffe00'} exec"
        elif cus == 'n':
            fdl_1 = await self.async_input("输入fdl1文件路径：")
            fdl_1_adr = await self.async_input("输入fdl1载入地址（默认为0x5000）:")
            fdl_2 = await self.async_input("输入fdl2文件路径：")
            fdl_2_adr = await self.async_input("输入fdl2载入地址（默认为0x9efffe00）:")
            kick = await self.async_input("是否需要使用SPRD4？（可能会擦除Splloader） (Y/n)")
            if kick == 'y':
                timeout = await self.async_input("输入超时时间：（默认为300s）")
                return f"dump.exe --kickto 2 --wait {timeout or '300'} fdl {fdl_1} {fdl_1_adr or '0x5000'} fdl {fdl_2} {fdl_2_adr or '0x9efffe00'} exec"
            elif kick == 'n':
                reattach = await self.async_input("是否使用重连？（SPRD4不支持）（Y/n）")
                if reattach == 'y':
                    timeout = await self.async_input("输入超时时间：（默认为30s）：")
                    return f"dump.exe -r --wait {timeout or '30'} fdl {fdl_1} {fdl_1_adr or '0x5000'} fdl {fdl_2} {fdl_2_adr or '0x9efffe00'} exec"
                elif reattach == 'n':
                    timeout = await self.async_input("输入超时时间：（默认为30s）：")
                    return f"dump.exe --wait {timeout or '30'} fdl {fdl_1} {fdl_1_adr or '0x5000'} fdl {fdl_2} {fdl_2_adr or '0x9efffe00'} exec"
        
    async def _resolve_command(self, raw_input):
        """解析并生成最终命令"""
        base_cmd = raw_input.strip().lower()
        #base_cmd = raw_input.strip().split(maxsplit=1).lower()
        if base_cmd not in self.command_handlers:
            return raw_input  # 非快捷命令直接返回

        handler = self.command_handlers[base_cmd]
        if callable(handler):
            # 执行带交互的命令处理器
            return await handler()
        return handler

    async def _handle_output(self, stream, prefix):
    #异步处理输出流
        while self.running:
            line = await stream.readline()
            if not line:
                await asyncio.sleep(0.1)
                continue
            # 修改解码方式为 GBK
            print(f"[{prefix}] {line.decode('gbk').strip()}")
    async def execute(self, command):
        """执行解析后的命令"""
        self.proc.stdin.write(f"{command}\r\n".encode())
        await self.proc.stdin.drain()

    async def start(self):
        """启动CMD进程"""
        self.proc = await asyncio.create_subprocess_exec(
            'cmd.exe', '/K',
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        asyncio.create_task(self._handle_output(self.proc.stdout, "STDOUT"))
        asyncio.create_task(self._handle_output(self.proc.stderr, "STDERR"))

    async def stop(self):
        """停止控制器"""
        self.running = False
        if self.proc:
            self.proc.terminate()
            await self.proc.wait()

async def interactive_mode():
    """增强型交互模式"""
    controller = CMDController()
    await controller.start()
    print("SPD Dump Runner Version 1.3.1 By Ryan Crepa q3285087232")
    print("命令：")
    print("  boot - 使用SC9832E模式引导设备")
    print("  boot-fdl - 使用自定义FDL引导设备")
    print("  boot-c - 使用配置文件引导")
    print("  w - 刷写分区（引导设备后）")
    print("  r - 回读分区（引导设备后）")
    print("  e - 格式化分区（引导设备后）（需要原厂RECOVERY）")
    print("  config - 编辑配置文件")
    print("  q - 退出\n")
    
    while controller.running:
        try:
            raw = await controller.async_input("$SDR> ")
            resolved = await controller._resolve_command(raw)
            
            if resolved.lower() in ('exit', 'q'):
                await controller.stop()
                break
                
            await controller.execute(resolved)
            
        except (KeyboardInterrupt, EOFError):
            await controller.stop()
            break

if __name__ == "__main__":
    try:
        asyncio.run(interactive_mode())
    except KeyboardInterrupt:
        print("\n安全退出")
