import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers

from kmk.extensions.ioexpander import IOExpander
from kmk.extensions.ioexpander.mcp230xx import MCP23017


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12
)

keyboard.row_pins = (board.GP13, board.GP14, board.GP15, board.GP16)

i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c=i2c, i2c_addr=0x20)
exp = IOExpander(mcp)

exp.col_pins = (0, 1, 2, 3, 4)
exp.row_pins = (8, 9, 10, 11, 12)

keyboard.extensions.append(exp)

keyboard.keymap = [
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.BSLS,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.MO(1), KC.ENT,

        KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS, KC.PGUP,
        KC.P7,   KC.P8,   KC.P9,   KC.PPLS, KC.HOME,
        KC.P4,   KC.P5,   KC.P6,   KC.PPLS, KC.END,
        KC.P1,   KC.P2,   KC.P3,   KC.PENT, KC.PGDN,
        KC.P0,   KC.PDOT, KC.PCMM, KC.MUTE, KC.DEL,
    ],
    [
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
        KC.TRNS, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.UNDS, KC.PLUS,
        KC.TRNS, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.PGUP, KC.HOME, KC.END,  KC.INS,  KC.DEL,  KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.MPRV, KC.MPLY, KC.MNXT, KC.VOLD, KC.VOLU, KC.MUTE, KC.BSPC, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.MPLY, KC.MPRV, KC.MNXT, KC.VOLD, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLU, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLU, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

keyboard.go()