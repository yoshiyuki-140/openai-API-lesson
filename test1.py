from openai import OpenAI
from local import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)

prompt = """
```c
#include <avr/io.h>
#include <avr/wdt.h>
#include <avr/interrupt.h>

#define CTOP  (0.65*F_CPU/1024-1)

ISR(TIMER2_COMPA_vect)
{
	if((~PINC & 0x30) != 0) {	// SWが押されているときは
		PORTD ^= 0x08;
	}
}

ISR(TIMER1_COMPA_vect)
{
	static unsigned char i = 0;

	OCR2A = ++i & 1 ? 64 : 80;
}

int main()
{
	DDRB = 0x3f;
	DDRC = 0x0f;
	DDRD = 0xf8;
	PORTB = 0xc0;
	PORTC = 0xf0;
	PORTD = 0x07;

	// Timer2
	TCCR2A = 0x02;	//
	TCCR2B = 0x05;	// CTC, 1/128
	OCR2A = 80;
	TCNT2 = 0;
	TIFR2 = 0x07;	// タイマフラグを全クリア
	TIMSK2 |= _BV(OCIE2A);	// 比較一致割り込み許可

	// Timer1
	TCCR1A = 0x00;	//
	TCCR1B = 0x0d;	// CTC, 1/1024
	OCR1A = CTOP;
	TCNT1 = 0;
	TIFR1 = 0x07;	// タイマフラグを全クリア
	TIMSK1 |= _BV(OCIE1A);	// 比較一致割り込み許可

	sei();
	for(;;) {
		wdt_reset();
	}
	return 0;
}
```
問:リスト4を改造し,スイッチが押されている間は単一音程（「ポー」）
を0.65秒ごとに断続(ON/OFF)するようにせよ,ただし,次の2通りで
実装せよ．

1. Timer1 割り込みの度に,Timer2 のカウント動作を開始・停止する方法

2. Timer1 割り込みの度に,Timer2 の割り込みを許可・禁止する方法
(Timer2のカウントアップ処理はそのまま継続)

"""

prompt = """
```
#include <avr/io.h>
#include <avr/wdt.h>
#include <avr/interrupt.h>

volatile unsigned char sw_cnt = 0;	// 値を確定するまでの繰り返し數
volatile unsigned char sw = 0;	// スイッチの確定値
volatile unsigned char sw_flag = 0;	// スイッチ状態の変化ビット
volatile unsigned char bz_flag = 0;	// ブザーON/OFF

// SW1,2 のピン変化で起動
ISR(PCINT1_vect)
{
	TCNT0 = 0;
	TIMSK0 |= _BV(TOIE0);	// タイマ0 OVF 割り込み有効化
}

// オーバーフローで起動
ISR(TIMER0_OVF_vect)
{
	unsigned char sw_new;

	sw_new = (~PINC >> 4) & 3;	// 最新の読み取り値
	sw_flag = sw ^ sw_new;	// スイッチのON/OFF変化を検出
	sw = sw_new;	// 読み取り値を更新

	TIMSK0 &= ~_BV(TOIE0);	// タイマ0 OVF 割り込み無効化
}

int main(void)
{
	unsigned char x = 0;

	DDRB = 0x3f;
	DDRC = 0x0f;
	DDRD = 0xf8;
	PORTB = 0xc0;
	PORTC = 0xf0;	// pull-up PC5,PC4
	PORTD = 0x37;

	PCMSK1 = 0x30;
	PCICR = _BV(PCIE1);

	// Timer0
	TCCR0A = 0x00;	// Normal
	TCCR0B = 0x05;	// 1/1024
	TIFR0 = 0x07;	// タイマフラグを全クリア

	sei();
	for(;;) {
		wdt_reset();

		if(sw_flag) { // スイッチが変化したときは
			switch (sw) {
			case 1:
				x = 0;
				break;	// 消灯
			case 2:
				x = 0x80 | (x >> 1);
				break;	// ドットを増やす
			}
			PORTB = x;
			PORTD = (x & 0xc0) | (PORTD & 0x3f);
			sw_flag = 0;
		}
	}
	return 0;
}
```
これからプリスケーラー値、TOP値、を求めよ
"""

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role":"system","content": prompt},
  ]
)

print(completion)
print(completion.choices[0].message)