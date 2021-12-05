Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=37,
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=38,
            module='common',
            names=[alias(name='PurchaseTestCommon', asname=None)],
            level=1,
        ),
        ClassDef(
            lineno=8,
            col_offset=0,
            end_lineno=42,
            end_col_offset=33,
            name='TestDeleteOrder',
            bases=[Name(lineno=8, col_offset=22, end_lineno=8, end_col_offset=40, id='PurchaseTestCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=10,
                    col_offset=4,
                    end_lineno=42,
                    end_col_offset=33,
                    name='test_00_delete_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=10, col_offset=29, end_lineno=10, end_col_offset=33, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=11,
                            col_offset=8,
                            end_lineno=11,
                            end_col_offset=76,
                            value=Constant(lineno=11, col_offset=8, end_lineno=11, end_col_offset=76, value=' Testcase for deleting purchase order with purchase user group', kind=None),
                        ),
                        Assign(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=72,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=15, id='partner', ctx=Store())],
                            value=Call(
                                lineno=14,
                                col_offset=18,
                                end_lineno=14,
                                end_col_offset=72,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=18,
                                    end_lineno=14,
                                    end_col_offset=48,
                                    value=Subscript(
                                        lineno=14,
                                        col_offset=18,
                                        end_lineno=14,
                                        end_col_offset=41,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=18,
                                            end_lineno=14,
                                            end_col_offset=26,
                                            value=Name(lineno=14, col_offset=18, end_lineno=14, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=14, col_offset=27, end_lineno=14, end_col_offset=40, value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=14,
                                        col_offset=49,
                                        end_lineno=14,
                                        end_col_offset=71,
                                        keys=[Constant(lineno=14, col_offset=50, end_lineno=14, end_col_offset=56, value='name', kind=None)],
                                        values=[Constant(lineno=14, col_offset=58, end_lineno=14, end_col_offset=70, value='My Partner', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=10,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=22, id='purchase_order', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=25,
                                end_lineno=19,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=25,
                                    end_lineno=16,
                                    end_col_offset=58,
                                    value=Subscript(
                                        lineno=16,
                                        col_offset=25,
                                        end_lineno=16,
                                        end_col_offset=51,
                                        value=Attribute(
                                            lineno=16,
                                            col_offset=25,
                                            end_lineno=16,
                                            end_col_offset=33,
                                            value=Name(lineno=16, col_offset=25, end_lineno=16, end_col_offset=29, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=16, col_offset=34, end_lineno=16, end_col_offset=50, value='purchase.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=16,
                                        col_offset=59,
                                        end_lineno=19,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=24, value='partner_id', kind=None),
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=19, value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                lineno=17,
                                                col_offset=26,
                                                end_lineno=17,
                                                end_col_offset=36,
                                                value=Name(lineno=17, col_offset=26, end_lineno=17, end_col_offset=33, id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=18, col_offset=21, end_lineno=18, end_col_offset=31, value='purchase', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=81,
                            targets=[Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=24, id='purchase_order_1', ctx=Store())],
                            value=Call(
                                lineno=20,
                                col_offset=27,
                                end_lineno=20,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=27,
                                    end_lineno=20,
                                    end_col_offset=51,
                                    value=Name(lineno=20, col_offset=27, end_lineno=20, end_col_offset=41, id='purchase_order', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=20,
                                        col_offset=52,
                                        end_lineno=20,
                                        end_col_offset=80,
                                        value=Name(lineno=20, col_offset=52, end_lineno=20, end_col_offset=56, id='self', ctx=Load()),
                                        attr='res_users_purchase_user',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            lineno=21,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=37,
                            items=[
                                withitem(
                                    context_expr=Call(
                                        lineno=21,
                                        col_offset=13,
                                        end_lineno=21,
                                        end_col_offset=41,
                                        func=Attribute(
                                            lineno=21,
                                            col_offset=13,
                                            end_lineno=21,
                                            end_col_offset=30,
                                            value=Name(lineno=21, col_offset=13, end_lineno=21, end_col_offset=17, id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=21, col_offset=31, end_lineno=21, end_col_offset=40, id='UserError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    lineno=22,
                                    col_offset=12,
                                    end_lineno=22,
                                    end_col_offset=37,
                                    value=Call(
                                        lineno=22,
                                        col_offset=12,
                                        end_lineno=22,
                                        end_col_offset=37,
                                        func=Attribute(
                                            lineno=22,
                                            col_offset=12,
                                            end_lineno=22,
                                            end_col_offset=35,
                                            value=Name(lineno=22, col_offset=12, end_lineno=22, end_col_offset=28, id='purchase_order_1', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=10,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=22, id='purchase_order', ctx=Store())],
                            value=Call(
                                lineno=25,
                                col_offset=25,
                                end_lineno=28,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=25,
                                    col_offset=25,
                                    end_lineno=25,
                                    end_col_offset=58,
                                    value=Subscript(
                                        lineno=25,
                                        col_offset=25,
                                        end_lineno=25,
                                        end_col_offset=51,
                                        value=Attribute(
                                            lineno=25,
                                            col_offset=25,
                                            end_lineno=25,
                                            end_col_offset=33,
                                            value=Name(lineno=25, col_offset=25, end_lineno=25, end_col_offset=29, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=25, col_offset=34, end_lineno=25, end_col_offset=50, value='purchase.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=25,
                                        col_offset=59,
                                        end_lineno=28,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=26, col_offset=12, end_lineno=26, end_col_offset=24, value='partner_id', kind=None),
                                            Constant(lineno=27, col_offset=12, end_lineno=27, end_col_offset=19, value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                lineno=26,
                                                col_offset=26,
                                                end_lineno=26,
                                                end_col_offset=36,
                                                value=Name(lineno=26, col_offset=26, end_lineno=26, end_col_offset=33, id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=27, col_offset=21, end_lineno=27, end_col_offset=31, value='purchase', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=29,
                            col_offset=8,
                            end_lineno=29,
                            end_col_offset=81,
                            targets=[Name(lineno=29, col_offset=8, end_lineno=29, end_col_offset=24, id='purchase_order_2', ctx=Store())],
                            value=Call(
                                lineno=29,
                                col_offset=27,
                                end_lineno=29,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=29,
                                    col_offset=27,
                                    end_lineno=29,
                                    end_col_offset=51,
                                    value=Name(lineno=29, col_offset=27, end_lineno=29, end_col_offset=41, id='purchase_order', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=29,
                                        col_offset=52,
                                        end_lineno=29,
                                        end_col_offset=80,
                                        value=Name(lineno=29, col_offset=52, end_lineno=29, end_col_offset=56, id='self', ctx=Load()),
                                        attr='res_users_purchase_user',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=40,
                            value=Call(
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=40,
                                func=Attribute(
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=38,
                                    value=Name(lineno=30, col_offset=8, end_lineno=30, end_col_offset=24, id='purchase_order_2', ctx=Load()),
                                    attr='button_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=31,
                            col_offset=8,
                            end_lineno=31,
                            end_col_offset=78,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=31,
                                    col_offset=8,
                                    end_lineno=31,
                                    end_col_offset=24,
                                    value=Name(lineno=31, col_offset=8, end_lineno=31, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=31,
                                        col_offset=25,
                                        end_lineno=31,
                                        end_col_offset=47,
                                        value=Name(lineno=31, col_offset=25, end_lineno=31, end_col_offset=41, id='purchase_order_2', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=31, col_offset=49, end_lineno=31, end_col_offset=57, value='cancel', kind=None),
                                    Constant(lineno=31, col_offset=59, end_lineno=31, end_col_offset=77, value='PO is cancelled!', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=33,
                            value=Call(
                                lineno=32,
                                col_offset=8,
                                end_lineno=32,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=8,
                                    end_lineno=32,
                                    end_col_offset=31,
                                    value=Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=24, id='purchase_order_2', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=35,
                            col_offset=8,
                            end_lineno=38,
                            end_col_offset=10,
                            targets=[Name(lineno=35, col_offset=8, end_lineno=35, end_col_offset=22, id='purchase_order', ctx=Store())],
                            value=Call(
                                lineno=35,
                                col_offset=25,
                                end_lineno=38,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=35,
                                    col_offset=25,
                                    end_lineno=35,
                                    end_col_offset=58,
                                    value=Subscript(
                                        lineno=35,
                                        col_offset=25,
                                        end_lineno=35,
                                        end_col_offset=51,
                                        value=Attribute(
                                            lineno=35,
                                            col_offset=25,
                                            end_lineno=35,
                                            end_col_offset=33,
                                            value=Name(lineno=35, col_offset=25, end_lineno=35, end_col_offset=29, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=35, col_offset=34, end_lineno=35, end_col_offset=50, value='purchase.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=35,
                                        col_offset=59,
                                        end_lineno=38,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=36, col_offset=12, end_lineno=36, end_col_offset=24, value='partner_id', kind=None),
                                            Constant(lineno=37, col_offset=12, end_lineno=37, end_col_offset=19, value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                lineno=36,
                                                col_offset=26,
                                                end_lineno=36,
                                                end_col_offset=36,
                                                value=Name(lineno=36, col_offset=26, end_lineno=36, end_col_offset=33, id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(lineno=37, col_offset=21, end_lineno=37, end_col_offset=28, value='draft', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=39,
                            col_offset=8,
                            end_lineno=39,
                            end_col_offset=81,
                            targets=[Name(lineno=39, col_offset=8, end_lineno=39, end_col_offset=24, id='purchase_order_3', ctx=Store())],
                            value=Call(
                                lineno=39,
                                col_offset=27,
                                end_lineno=39,
                                end_col_offset=81,
                                func=Attribute(
                                    lineno=39,
                                    col_offset=27,
                                    end_lineno=39,
                                    end_col_offset=51,
                                    value=Name(lineno=39, col_offset=27, end_lineno=39, end_col_offset=41, id='purchase_order', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=39,
                                        col_offset=52,
                                        end_lineno=39,
                                        end_col_offset=80,
                                        value=Name(lineno=39, col_offset=52, end_lineno=39, end_col_offset=56, id='self', ctx=Load()),
                                        attr='res_users_purchase_user',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=40,
                            col_offset=8,
                            end_lineno=40,
                            end_col_offset=40,
                            value=Call(
                                lineno=40,
                                col_offset=8,
                                end_lineno=40,
                                end_col_offset=40,
                                func=Attribute(
                                    lineno=40,
                                    col_offset=8,
                                    end_lineno=40,
                                    end_col_offset=38,
                                    value=Name(lineno=40, col_offset=8, end_lineno=40, end_col_offset=24, id='purchase_order_3', ctx=Load()),
                                    attr='button_cancel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=41,
                            col_offset=8,
                            end_lineno=41,
                            end_col_offset=78,
                            value=Call(
                                lineno=41,
                                col_offset=8,
                                end_lineno=41,
                                end_col_offset=78,
                                func=Attribute(
                                    lineno=41,
                                    col_offset=8,
                                    end_lineno=41,
                                    end_col_offset=24,
                                    value=Name(lineno=41, col_offset=8, end_lineno=41, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=41,
                                        col_offset=25,
                                        end_lineno=41,
                                        end_col_offset=47,
                                        value=Name(lineno=41, col_offset=25, end_lineno=41, end_col_offset=41, id='purchase_order_3', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=41, col_offset=49, end_lineno=41, end_col_offset=57, value='cancel', kind=None),
                                    Constant(lineno=41, col_offset=59, end_lineno=41, end_col_offset=77, value='PO is cancelled!', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=42,
                            col_offset=8,
                            end_lineno=42,
                            end_col_offset=33,
                            value=Call(
                                lineno=42,
                                col_offset=8,
                                end_lineno=42,
                                end_col_offset=33,
                                func=Attribute(
                                    lineno=42,
                                    col_offset=8,
                                    end_lineno=42,
                                    end_col_offset=31,
                                    value=Name(lineno=42, col_offset=8, end_lineno=42, end_col_offset=24, id='purchase_order_3', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)