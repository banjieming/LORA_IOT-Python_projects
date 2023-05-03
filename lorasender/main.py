#!/usr/bin/env Python3 
# -*- coding: utf-8 -*-
import gc
gc.collect()

import sx127x
gc.collect()

import config_lora
gc.collect()

# import LoRaDumpRegisters
# import LoRaSender
# import LoRaReceiver
# import LoRaSetSpread
# import LoRaSetSyncWord
# import LoRaReceiverCallback
# import LoRaDuplex
#import LoRaDuplexCallback
# import LoRaPingPong
from time import sleep
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
thisNodeaddr=0x0
thisGatewayaddr=0x01
destinationNodeaddr=0x0
destinationGatewayaddr=0x0

def main(): 
    
    # Controller(
               # pin_id_led = ON_BOARD_LED_PIN_NO, 
               # on_board_led_high_is_on = ON_BOARD_LED_HIGH_IS_ON,
               # pin_id_reset = PIN_ID_FOR_LORA_RESET, 
               # blink_on_start = (2, 0.5, 0.5))
    controller = config_lora.Controller()
    
    
    #SX127x(name = 'SX127x',
           # parameters = {'frequency': 433E6, 'tx_power_level': 2, 'signal_bandwidth': 125E3,
                         # 'spreading_factor': 7, 'coding_rate': 5, 'preamble_length': 8,
                         # 'implicitHeader': False, 'sync_word': 0x12, 'enable_CRC': True},
           # onReceive = None)
           
    # controller.add_transceiver(transceiver,
                               # pin_id_ss = PIN_ID_FOR_LORA_SS,
                               # pin_id_RxDone = PIN_ID_FOR_LORA_DIO0,
                               # pin_id_RxTimeout = PIN_ID_FOR_LORA_DIO1,
                               # pin_id_ValidHeader = PIN_ID_FOR_LORA_DIO2,
                               # pin_id_CadDone = PIN_ID_FOR_LORA_DIO3,
                               # pin_id_CadDetected = PIN_ID_FOR_LORA_DIO4,
                               # pin_id_PayloadCrcError = PIN_ID_FOR_LORA_DIO5)
                             
    lora = controller.add_transceiver(sx127x.SX127x(name = 'C100E026',
                                                    parameters = {'frequency': 438E6, 'tx_power_level': 23, 'signal_bandwidth': 125E3,
                                                                  'spreading_factor': 7, 'coding_rate': 5, 'preamble_length': 8,
                                                                  'implicitHeader': False, 'sync_word': 0x12, 'enable_CRC': True}),
                                      pin_id_ss = config_lora.Controller.PIN_ID_FOR_LORA_SS,
                                      pin_id_RxDone = config_lora.Controller.PIN_ID_FOR_LORA_DIO0)

    #lora = controller.add_transceiver(sx127x.SX127x(name ='LoRaNode'),
                                      # pin_id_ss = config_lora.Controller.PIN_ID_FOR_LORA_SS,
                                      # pin_id_RxDone = config_lora.Controller.PIN_ID_FOR_LORA_DIO0)
    #lora.enableCRC(True)
    for i in range(40):
        print("0x{0:02x}: {1:02x}".format(i, lora.readRegister(i)))
    
    print(lora.name, lora)
    # LoRaDumpRegisters.dumpRegisters(lora)
    import LoRaSender
    LoRaSender.do_loop(lora)
    #import LoRaReceiver
    #LoRaReceiver.receive(lora)
    # LoRaSetSpread.setSpread(lora)
    # LoRaSetSyncWord.setSyncWord(lora)
    #import LoRaGatewayCallback
    #LoRaGatewayCallback.gatewayCallback(lora)
    #import LoRaRepeaterCallback
    #LoRaRepeaterCallback.gatewayCallback(lora)
    # import LoRaReceiverCallback
    # LoRaReceiverCallback.receiveCallback(lora)
    # LoRaDuplex.duplex(lora)
    # LoRaDuplexCallback.duplexCallback(lora)
    # LoRaPingPong.ping_pong(lora)
    # import LoRaDuplex
    # LoRaDuplex.duplex(lora)
    # from LoRaSender import sendmesg
    # sendmesg(lora)
    
if __name__ == '__main__':
    main()