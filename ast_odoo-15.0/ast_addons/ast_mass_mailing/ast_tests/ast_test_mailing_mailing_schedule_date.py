Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=29,
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=64,
            module='odoo.addons.mass_mailing.tests.common',
            names=[alias(name='MassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=34,
            module='odoo.tests',
            names=[
                alias(name='users', asname=None),
                alias(name='Form', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=34,
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=11,
            col_offset=0,
            end_lineno=33,
            end_col_offset=51,
            name='TestMailingScheduleDateWizard',
            bases=[Name(lineno=11, col_offset=36, end_lineno=11, end_col_offset=50, id='MassMailCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=15,
                    col_offset=4,
                    end_lineno=33,
                    end_col_offset=51,
                    name='test_mailing_schedule_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=15, col_offset=35, end_lineno=15, end_col_offset=39, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=16,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=10,
                            targets=[Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=15, id='mailing', ctx=Store())],
                            value=Call(
                                lineno=16,
                                col_offset=18,
                                end_lineno=20,
                                end_col_offset=10,
                                func=Attribute(
                                    lineno=16,
                                    col_offset=18,
                                    end_lineno=16,
                                    end_col_offset=52,
                                    value=Subscript(
                                        lineno=16,
                                        col_offset=18,
                                        end_lineno=16,
                                        end_col_offset=45,
                                        value=Attribute(
                                            lineno=16,
                                            col_offset=18,
                                            end_lineno=16,
                                            end_col_offset=26,
                                            value=Name(lineno=16, col_offset=18, end_lineno=16, end_col_offset=22, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=16, col_offset=27, end_lineno=16, end_col_offset=44, value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        lineno=16,
                                        col_offset=53,
                                        end_lineno=20,
                                        end_col_offset=9,
                                        keys=[
                                            Constant(lineno=17, col_offset=12, end_lineno=17, end_col_offset=18, value='name', kind=None),
                                            Constant(lineno=18, col_offset=12, end_lineno=18, end_col_offset=21, value='subject', kind=None),
                                            Constant(lineno=19, col_offset=12, end_lineno=19, end_col_offset=30, value='mailing_model_id', kind=None),
                                        ],
                                        values=[
                                            Constant(lineno=17, col_offset=20, end_lineno=17, end_col_offset=29, value='mailing', kind=None),
                                            Constant(lineno=18, col_offset=23, end_lineno=18, end_col_offset=37, value='some subject', kind=None),
                                            Attribute(
                                                lineno=19,
                                                col_offset=32,
                                                end_lineno=19,
                                                end_col_offset=75,
                                                value=Call(
                                                    lineno=19,
                                                    col_offset=32,
                                                    end_lineno=19,
                                                    end_col_offset=72,
                                                    func=Attribute(
                                                        lineno=19,
                                                        col_offset=32,
                                                        end_lineno=19,
                                                        end_col_offset=57,
                                                        value=Subscript(
                                                            lineno=19,
                                                            col_offset=32,
                                                            end_lineno=19,
                                                            end_col_offset=52,
                                                            value=Attribute(
                                                                lineno=19,
                                                                col_offset=32,
                                                                end_lineno=19,
                                                                end_col_offset=40,
                                                                value=Name(lineno=19, col_offset=32, end_lineno=19, end_col_offset=36, id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(lineno=19, col_offset=41, end_lineno=19, end_col_offset=51, value='ir.model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(lineno=19, col_offset=58, end_lineno=19, end_col_offset=71, value='res.partner', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=22,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=103,
                            targets=[Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=19, id='wizard_form', ctx=Store())],
                            value=Call(
                                lineno=22,
                                col_offset=22,
                                end_lineno=23,
                                end_col_offset=103,
                                func=Name(lineno=22, col_offset=22, end_lineno=22, end_col_offset=26, id='Form', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=23,
                                        col_offset=12,
                                        end_lineno=23,
                                        end_col_offset=102,
                                        func=Attribute(
                                            lineno=23,
                                            col_offset=12,
                                            end_lineno=23,
                                            end_col_offset=66,
                                            value=Subscript(
                                                lineno=23,
                                                col_offset=12,
                                                end_lineno=23,
                                                end_col_offset=53,
                                                value=Attribute(
                                                    lineno=23,
                                                    col_offset=12,
                                                    end_lineno=23,
                                                    end_col_offset=20,
                                                    value=Name(lineno=23, col_offset=12, end_lineno=23, end_col_offset=16, id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(lineno=23, col_offset=21, end_lineno=23, end_col_offset=52, value='mailing.mailing.schedule.date', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                lineno=23,
                                                col_offset=67,
                                                end_lineno=23,
                                                end_col_offset=101,
                                                arg='default_mass_mailing_id',
                                                value=Attribute(
                                                    lineno=23,
                                                    col_offset=91,
                                                    end_lineno=23,
                                                    end_col_offset=101,
                                                    value=Name(lineno=23, col_offset=91, end_lineno=23, end_col_offset=98, id='mailing', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=63,
                            targets=[
                                Attribute(
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=33,
                                    value=Name(lineno=26, col_offset=8, end_lineno=26, end_col_offset=19, id='wizard_form', ctx=Load()),
                                    attr='schedule_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=26,
                                col_offset=36,
                                end_lineno=26,
                                end_col_offset=63,
                                func=Name(lineno=26, col_offset=36, end_lineno=26, end_col_offset=44, id='datetime', ctx=Load()),
                                args=[
                                    Constant(lineno=26, col_offset=45, end_lineno=26, end_col_offset=49, value=2021, kind=None),
                                    Constant(lineno=26, col_offset=51, end_lineno=26, end_col_offset=52, value=4, kind=None),
                                    Constant(lineno=26, col_offset=54, end_lineno=26, end_col_offset=56, value=30, kind=None),
                                    Constant(lineno=26, col_offset=58, end_lineno=26, end_col_offset=59, value=9, kind=None),
                                    Constant(lineno=26, col_offset=61, end_lineno=26, end_col_offset=62, value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=35,
                            targets=[Name(lineno=27, col_offset=8, end_lineno=27, end_col_offset=14, id='wizard', ctx=Store())],
                            value=Call(
                                lineno=27,
                                col_offset=17,
                                end_lineno=27,
                                end_col_offset=35,
                                func=Attribute(
                                    lineno=27,
                                    col_offset=17,
                                    end_lineno=27,
                                    end_col_offset=33,
                                    value=Name(lineno=27, col_offset=17, end_lineno=27, end_col_offset=28, id='wizard_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=28,
                            col_offset=8,
                            end_lineno=28,
                            end_col_offset=37,
                            value=Call(
                                lineno=28,
                                col_offset=8,
                                end_lineno=28,
                                end_col_offset=37,
                                func=Attribute(
                                    lineno=28,
                                    col_offset=8,
                                    end_lineno=28,
                                    end_col_offset=35,
                                    value=Name(lineno=28, col_offset=8, end_lineno=28, end_col_offset=14, id='wizard', ctx=Load()),
                                    attr='action_schedule_date',
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
                            end_col_offset=76,
                            value=Call(
                                lineno=31,
                                col_offset=8,
                                end_lineno=31,
                                end_col_offset=76,
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
                                        end_col_offset=46,
                                        value=Name(lineno=31, col_offset=25, end_lineno=31, end_col_offset=32, id='mailing', ctx=Load()),
                                        attr='schedule_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        lineno=31,
                                        col_offset=48,
                                        end_lineno=31,
                                        end_col_offset=75,
                                        func=Name(lineno=31, col_offset=48, end_lineno=31, end_col_offset=56, id='datetime', ctx=Load()),
                                        args=[
                                            Constant(lineno=31, col_offset=57, end_lineno=31, end_col_offset=61, value=2021, kind=None),
                                            Constant(lineno=31, col_offset=63, end_lineno=31, end_col_offset=64, value=4, kind=None),
                                            Constant(lineno=31, col_offset=66, end_lineno=31, end_col_offset=68, value=30, kind=None),
                                            Constant(lineno=31, col_offset=70, end_lineno=31, end_col_offset=71, value=9, kind=None),
                                            Constant(lineno=31, col_offset=73, end_lineno=31, end_col_offset=74, value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=32,
                            col_offset=8,
                            end_lineno=32,
                            end_col_offset=60,
                            value=Call(
                                lineno=32,
                                col_offset=8,
                                end_lineno=32,
                                end_col_offset=60,
                                func=Attribute(
                                    lineno=32,
                                    col_offset=8,
                                    end_lineno=32,
                                    end_col_offset=24,
                                    value=Name(lineno=32, col_offset=8, end_lineno=32, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=32,
                                        col_offset=25,
                                        end_lineno=32,
                                        end_col_offset=46,
                                        value=Name(lineno=32, col_offset=25, end_lineno=32, end_col_offset=32, id='mailing', ctx=Load()),
                                        attr='schedule_type',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=32, col_offset=48, end_lineno=32, end_col_offset=59, value='scheduled', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=51,
                            value=Call(
                                lineno=33,
                                col_offset=8,
                                end_lineno=33,
                                end_col_offset=51,
                                func=Attribute(
                                    lineno=33,
                                    col_offset=8,
                                    end_lineno=33,
                                    end_col_offset=24,
                                    value=Name(lineno=33, col_offset=8, end_lineno=33, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=33,
                                        col_offset=25,
                                        end_lineno=33,
                                        end_col_offset=38,
                                        value=Name(lineno=33, col_offset=25, end_lineno=33, end_col_offset=32, id='mailing', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(lineno=33, col_offset=40, end_lineno=33, end_col_offset=50, value='in_queue', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            lineno=13,
                            col_offset=5,
                            end_lineno=13,
                            end_col_offset=53,
                            func=Name(lineno=13, col_offset=5, end_lineno=13, end_col_offset=16, id='mute_logger', ctx=Load()),
                            args=[Constant(lineno=13, col_offset=17, end_lineno=13, end_col_offset=52, value='odoo.addons.mail.models.mail_mail', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            lineno=14,
                            col_offset=5,
                            end_lineno=14,
                            end_col_offset=28,
                            func=Name(lineno=14, col_offset=5, end_lineno=14, end_col_offset=10, id='users', ctx=Load()),
                            args=[Constant(lineno=14, col_offset=11, end_lineno=14, end_col_offset=27, value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)