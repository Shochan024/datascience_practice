#!-*-coding:utf-8-*-
__all__ = ["txt_count"]

def txt_count( files , text , encoding="utf-8" ):
    """
    filesに含まれているファイルに、textで指定した文字列が入っているかカウントする
    -- input
      ・ files : list
      ・ text : string
      ・ encodging : string
    -- return
      ・ dict
    """

    count = 0
    for file in files:
        with open( file , encoding=encoding ) as f:
            line = f.read()
            if text in line:
                count += 1

    return { "freq":count,"N":len(files) }


def txt_vec( files , text , encoding="utf-8" ):
        """
        filesに含まれているファイルに、textで指定した文字列が入っていれば1を出力する
        -- input
          ・ files : list
          ・ text : string
          ・ encodging : string
        -- return
          ・ integer
        """
        for file in files:
            with open( file , encoding=encoding ) as f:
                line = f.read()
                if text in line:
                    return 1
                else:
                    return 0
