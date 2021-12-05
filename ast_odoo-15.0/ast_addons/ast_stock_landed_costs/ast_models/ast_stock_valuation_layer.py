Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=12,
            end_col_offset=78,
            name='StockValuationLayer',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=26,
                    end_lineno=7,
                    end_col_offset=38,
                    value=Name(lineno=7, col_offset=26, end_lineno=7, end_col_offset=32, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=31,
                    value=Constant(lineno=8, col_offset=4, end_lineno=8, end_col_offset=31, value='Stock Valuation Layer', kind=None),
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=38,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=10, col_offset=15, end_lineno=10, end_col_offset=38, value='stock.valuation.layer', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=78,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=24, id='stock_landed_cost_id', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=27,
                        end_lineno=12,
                        end_col_offset=78,
                        func=Attribute(
                            lineno=12,
                            col_offset=27,
                            end_lineno=12,
                            end_col_offset=42,
                            value=Name(lineno=12, col_offset=27, end_lineno=12, end_col_offset=33, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(lineno=12, col_offset=43, end_lineno=12, end_col_offset=62, value='stock.landed.cost', kind=None),
                            Constant(lineno=12, col_offset=64, end_lineno=12, end_col_offset=77, value='Landed Cost', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)