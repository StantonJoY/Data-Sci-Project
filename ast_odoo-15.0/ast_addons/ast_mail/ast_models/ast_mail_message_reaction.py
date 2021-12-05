Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=24,
            end_col_offset=5,
            name='MailMessageReaction',
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
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=35,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=8, col_offset=12, end_lineno=8, end_col_offset=35, value='mail.message.reaction', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=37,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=9, col_offset=19, end_lineno=9, end_col_offset=37, value='Message Reaction', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=22,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=10, col_offset=13, end_lineno=10, end_col_offset=22, value='id desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=23,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=15, id='_log_access', ctx=Store())],
                    value=Constant(lineno=11, col_offset=18, end_lineno=11, end_col_offset=23, value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=129,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=14, id='message_id', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=17,
                        end_lineno=13,
                        end_col_offset=129,
                        func=Attribute(
                            lineno=13,
                            col_offset=17,
                            end_lineno=13,
                            end_col_offset=32,
                            value=Name(lineno=13, col_offset=17, end_lineno=13, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=33,
                                end_lineno=13,
                                end_col_offset=49,
                                arg='string',
                                value=Constant(lineno=13, col_offset=40, end_lineno=13, end_col_offset=49, value='Message', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=51,
                                end_lineno=13,
                                end_col_offset=78,
                                arg='comodel_name',
                                value=Constant(lineno=13, col_offset=64, end_lineno=13, end_col_offset=78, value='mail.message', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=80,
                                end_lineno=13,
                                end_col_offset=98,
                                arg='ondelete',
                                value=Constant(lineno=13, col_offset=89, end_lineno=13, end_col_offset=98, value='cascade', kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=100,
                                end_lineno=13,
                                end_col_offset=113,
                                arg='required',
                                value=Constant(lineno=13, col_offset=109, end_lineno=13, end_col_offset=113, value=True, kind=None),
                            ),
                            keyword(
                                lineno=13,
                                col_offset=115,
                                end_lineno=13,
                                end_col_offset=128,
                                arg='readonly',
                                value=Constant(lineno=13, col_offset=124, end_lineno=13, end_col_offset=128, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=73,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=11, id='content', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=14,
                        end_lineno=14,
                        end_col_offset=73,
                        func=Attribute(
                            lineno=14,
                            col_offset=14,
                            end_lineno=14,
                            end_col_offset=25,
                            value=Name(lineno=14, col_offset=14, end_lineno=14, end_col_offset=20, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=26,
                                end_lineno=14,
                                end_col_offset=42,
                                arg='string',
                                value=Constant(lineno=14, col_offset=33, end_lineno=14, end_col_offset=42, value='Content', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=44,
                                end_lineno=14,
                                end_col_offset=57,
                                arg='required',
                                value=Constant(lineno=14, col_offset=53, end_lineno=14, end_col_offset=57, value=True, kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=59,
                                end_lineno=14,
                                end_col_offset=72,
                                arg='readonly',
                                value=Constant(lineno=14, col_offset=68, end_lineno=14, end_col_offset=72, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=15,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=122,
                    targets=[Name(lineno=15, col_offset=4, end_lineno=15, end_col_offset=14, id='partner_id', ctx=Store())],
                    value=Call(
                        lineno=15,
                        col_offset=17,
                        end_lineno=15,
                        end_col_offset=122,
                        func=Attribute(
                            lineno=15,
                            col_offset=17,
                            end_lineno=15,
                            end_col_offset=32,
                            value=Name(lineno=15, col_offset=17, end_lineno=15, end_col_offset=23, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=15,
                                col_offset=33,
                                end_lineno=15,
                                end_col_offset=58,
                                arg='string',
                                value=Constant(lineno=15, col_offset=40, end_lineno=15, end_col_offset=58, value='Reacting Partner', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=60,
                                end_lineno=15,
                                end_col_offset=86,
                                arg='comodel_name',
                                value=Constant(lineno=15, col_offset=73, end_lineno=15, end_col_offset=86, value='res.partner', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=88,
                                end_lineno=15,
                                end_col_offset=106,
                                arg='ondelete',
                                value=Constant(lineno=15, col_offset=97, end_lineno=15, end_col_offset=106, value='cascade', kind=None),
                            ),
                            keyword(
                                lineno=15,
                                col_offset=108,
                                end_lineno=15,
                                end_col_offset=121,
                                arg='readonly',
                                value=Constant(lineno=15, col_offset=117, end_lineno=15, end_col_offset=121, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=16,
                    col_offset=4,
                    end_lineno=16,
                    end_col_offset=117,
                    targets=[Name(lineno=16, col_offset=4, end_lineno=16, end_col_offset=12, id='guest_id', ctx=Store())],
                    value=Call(
                        lineno=16,
                        col_offset=15,
                        end_lineno=16,
                        end_col_offset=117,
                        func=Attribute(
                            lineno=16,
                            col_offset=15,
                            end_lineno=16,
                            end_col_offset=30,
                            value=Name(lineno=16, col_offset=15, end_lineno=16, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=16,
                                col_offset=31,
                                end_lineno=16,
                                end_col_offset=54,
                                arg='string',
                                value=Constant(lineno=16, col_offset=38, end_lineno=16, end_col_offset=54, value='Reacting Guest', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=56,
                                end_lineno=16,
                                end_col_offset=81,
                                arg='comodel_name',
                                value=Constant(lineno=16, col_offset=69, end_lineno=16, end_col_offset=81, value='mail.guest', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=83,
                                end_lineno=16,
                                end_col_offset=101,
                                arg='ondelete',
                                value=Constant(lineno=16, col_offset=92, end_lineno=16, end_col_offset=101, value='cascade', kind=None),
                            ),
                            keyword(
                                lineno=16,
                                col_offset=103,
                                end_lineno=16,
                                end_col_offset=116,
                                arg='readonly',
                                value=Constant(lineno=16, col_offset=112, end_lineno=16, end_col_offset=116, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=18,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=178,
                    name='init',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=18, col_offset=13, end_lineno=18, end_col_offset=17, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            lineno=19,
                            col_offset=8,
                            end_lineno=19,
                            end_col_offset=184,
                            value=Call(
                                lineno=19,
                                col_offset=8,
                                end_lineno=19,
                                end_col_offset=184,
                                func=Attribute(
                                    lineno=19,
                                    col_offset=8,
                                    end_lineno=19,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=19,
                                        col_offset=8,
                                        end_lineno=19,
                                        end_col_offset=19,
                                        value=Attribute(
                                            lineno=19,
                                            col_offset=8,
                                            end_lineno=19,
                                            end_col_offset=16,
                                            value=Name(lineno=19, col_offset=8, end_lineno=19, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=19,
                                        col_offset=28,
                                        end_lineno=19,
                                        end_col_offset=183,
                                        left=Constant(lineno=19, col_offset=28, end_lineno=19, end_col_offset=169, value='CREATE UNIQUE INDEX IF NOT EXISTS mail_message_reaction_partner_unique ON %s (message_id, content, partner_id) WHERE partner_id IS NOT NULL', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            lineno=19,
                                            col_offset=172,
                                            end_lineno=19,
                                            end_col_offset=183,
                                            value=Name(lineno=19, col_offset=172, end_lineno=19, end_col_offset=176, id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=178,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=178,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=27,
                                    value=Attribute(
                                        lineno=20,
                                        col_offset=8,
                                        end_lineno=20,
                                        end_col_offset=19,
                                        value=Attribute(
                                            lineno=20,
                                            col_offset=8,
                                            end_lineno=20,
                                            end_col_offset=16,
                                            value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=20,
                                        col_offset=28,
                                        end_lineno=20,
                                        end_col_offset=177,
                                        left=Constant(lineno=20, col_offset=28, end_lineno=20, end_col_offset=163, value='CREATE UNIQUE INDEX IF NOT EXISTS mail_message_reaction_guest_unique ON %s (message_id, content, guest_id) WHERE guest_id IS NOT NULL', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            lineno=20,
                                            col_offset=166,
                                            end_lineno=20,
                                            end_col_offset=177,
                                            value=Name(lineno=20, col_offset=166, end_lineno=20, end_col_offset=170, id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=24,
                    end_col_offset=5,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=20, id='_sql_constraints', ctx=Store())],
                    value=List(
                        lineno=22,
                        col_offset=23,
                        end_lineno=24,
                        end_col_offset=5,
                        elts=[
                            Tuple(
                                lineno=23,
                                col_offset=8,
                                end_lineno=23,
                                end_col_offset=202,
                                elts=[
                                    Constant(lineno=23, col_offset=9, end_lineno=23, end_col_offset=34, value='partner_or_guest_exists', kind=None),
                                    Constant(lineno=23, col_offset=36, end_lineno=23, end_col_offset=139, value='CHECK((partner_id IS NOT NULL AND guest_id IS NULL) OR (partner_id IS NULL AND guest_id IS NOT NULL))', kind=None),
                                    Constant(lineno=23, col_offset=141, end_lineno=23, end_col_offset=201, value='A message reaction must be from a partner or from a guest.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)