import sys
args = sys.argv
from create_trasport import session
from create_trasport import Transport

ins_date = int(args[1])     #日付を取得
ins_seq = int(args[2])      #連番を取得
ins_departure = args[3]     #出発地を取得
ins_arrival = args[4]       #到着地を取得
ins_via = args[5]           #経由/利用交通機関の取得
ins_amount = int(args[6])   #金額を取得

def check_data(ins_date, ins_seq):      #重複がないかの確認をする関数を定義
    date_frag = session.query(Transport.date)\
        .filter_by(date = ins_date).count()    #日付の重複がないかを確認
    seq_frag = session.query(Transport.seq)\
        .filter_by(seq = ins_seq).count() 
    frag = [date_frag, seq_frag]       #重複のフラグリストを作成
    return frag    #重複確認のフラグを返す

frag = check_data(ins_date, ins_seq)      #重複確認の関数を呼び出す
if frag[0]== 1 and frag[1] == 1:        #重複している場合
    print("error:交通費精算テーブルにデータを登録できませんでした")
else:       #重複がない場合
    transport = Transport(
        date = ins_date, seq = ins_seq, departure = ins_departure,\
              arrival = ins_arrival, via = ins_via, amount = ins_amount     #データベースに登録
    )

    session.add(transport)

    session.commit()
