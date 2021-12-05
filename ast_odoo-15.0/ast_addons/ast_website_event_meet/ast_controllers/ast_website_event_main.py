Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=39,
            module='babel.dates',
            names=[alias(name='format_datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=18,
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=29,
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=54,
            module='odoo.addons.website_event.controllers',
            names=[alias(name='main', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=11,
            col_offset=0,
            end_lineno=25,
            end_col_offset=21,
            name='WebsiteEventController',
            bases=[
                Attribute(
                    lineno=11,
                    col_offset=29,
                    end_lineno=11,
                    end_col_offset=56,
                    value=Name(lineno=11, col_offset=29, end_lineno=11, end_col_offset=33, id='main', ctx=Load()),
                    attr='WebsiteEventController',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=12,
                    col_offset=4,
                    end_lineno=25,
                    end_col_offset=21,
                    name='_prepare_event_register_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=12, col_offset=39, end_lineno=12, end_col_offset=43, arg='self', annotation=None, type_comment=None),
                            arg(lineno=12, col_offset=45, end_lineno=12, end_col_offset=50, arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(lineno=12, col_offset=54, end_lineno=12, end_col_offset=58, arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=13,
                            col_offset=8,
                            end_lineno=13,
                            end_col_offset=98,
                            targets=[Name(lineno=13, col_offset=8, end_lineno=13, end_col_offset=14, id='values', ctx=Store())],
                            value=Call(
                                lineno=13,
                                col_offset=17,
                                end_lineno=13,
                                end_col_offset=98,
                                func=Attribute(
                                    lineno=13,
                                    col_offset=17,
                                    end_lineno=13,
                                    end_col_offset=83,
                                    value=Call(
                                        lineno=13,
                                        col_offset=17,
                                        end_lineno=13,
                                        end_col_offset=52,
                                        func=Name(lineno=13, col_offset=17, end_lineno=13, end_col_offset=22, id='super', ctx=Load()),
                                        args=[
                                            Name(lineno=13, col_offset=23, end_lineno=13, end_col_offset=45, id='WebsiteEventController', ctx=Load()),
                                            Name(lineno=13, col_offset=47, end_lineno=13, end_col_offset=51, id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_event_register_values',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=13, col_offset=84, end_lineno=13, end_col_offset=89, id='event', ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=13,
                                        col_offset=91,
                                        end_lineno=13,
                                        end_col_offset=97,
                                        arg=None,
                                        value=Name(lineno=13, col_offset=93, end_lineno=13, end_col_offset=97, id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            lineno=15,
                            col_offset=8,
                            end_lineno=23,
                            end_col_offset=17,
                            test=BoolOp(
                                lineno=15,
                                col_offset=11,
                                end_lineno=15,
                                end_col_offset=58,
                                op=And(),
                                values=[
                                    Compare(
                                        lineno=15,
                                        col_offset=11,
                                        end_lineno=15,
                                        end_col_offset=33,
                                        left=Constant(lineno=15, col_offset=11, end_lineno=15, end_col_offset=25, value='from_room_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(lineno=15, col_offset=29, end_lineno=15, end_col_offset=33, id='post', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        lineno=15,
                                        col_offset=38,
                                        end_lineno=15,
                                        end_col_offset=58,
                                        op=Not(),
                                        operand=Attribute(
                                            lineno=15,
                                            col_offset=42,
                                            end_lineno=15,
                                            end_col_offset=58,
                                            value=Name(lineno=15, col_offset=42, end_lineno=15, end_col_offset=47, id='event', ctx=Load()),
                                            attr='is_ongoing',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    lineno=16,
                                    col_offset=12,
                                    end_lineno=16,
                                    end_col_offset=110,
                                    targets=[Name(lineno=16, col_offset=12, end_lineno=16, end_col_offset=24, id='meeting_room', ctx=Store())],
                                    value=Call(
                                        lineno=16,
                                        col_offset=27,
                                        end_lineno=16,
                                        end_col_offset=110,
                                        func=Attribute(
                                            lineno=16,
                                            col_offset=27,
                                            end_lineno=16,
                                            end_col_offset=108,
                                            value=Call(
                                                lineno=16,
                                                col_offset=27,
                                                end_lineno=16,
                                                end_col_offset=101,
                                                func=Attribute(
                                                    lineno=16,
                                                    col_offset=27,
                                                    end_lineno=16,
                                                    end_col_offset=99,
                                                    value=Call(
                                                        lineno=16,
                                                        col_offset=27,
                                                        end_lineno=16,
                                                        end_col_offset=94,
                                                        func=Attribute(
                                                            lineno=16,
                                                            col_offset=27,
                                                            end_lineno=16,
                                                            end_col_offset=67,
                                                            value=Subscript(
                                                                lineno=16,
                                                                col_offset=27,
                                                                end_lineno=16,
                                                                end_col_offset=60,
                                                                value=Attribute(
                                                                    lineno=16,
                                                                    col_offset=27,
                                                                    end_lineno=16,
                                                                    end_col_offset=38,
                                                                    value=Name(lineno=16, col_offset=27, end_lineno=16, end_col_offset=34, id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(lineno=16, col_offset=39, end_lineno=16, end_col_offset=59, value='event.meeting.room', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                lineno=16,
                                                                col_offset=68,
                                                                end_lineno=16,
                                                                end_col_offset=93,
                                                                func=Name(lineno=16, col_offset=68, end_lineno=16, end_col_offset=71, id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        lineno=16,
                                                                        col_offset=72,
                                                                        end_lineno=16,
                                                                        end_col_offset=92,
                                                                        value=Name(lineno=16, col_offset=72, end_lineno=16, end_col_offset=76, id='post', ctx=Load()),
                                                                        slice=Constant(lineno=16, col_offset=77, end_lineno=16, end_col_offset=91, value='from_room_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    lineno=17,
                                    col_offset=12,
                                    end_lineno=23,
                                    end_col_offset=17,
                                    test=BoolOp(
                                        lineno=17,
                                        col_offset=15,
                                        end_lineno=17,
                                        end_col_offset=57,
                                        op=And(),
                                        values=[
                                            Name(lineno=17, col_offset=15, end_lineno=17, end_col_offset=27, id='meeting_room', ctx=Load()),
                                            Attribute(
                                                lineno=17,
                                                col_offset=32,
                                                end_lineno=17,
                                                end_col_offset=57,
                                                value=Name(lineno=17, col_offset=32, end_lineno=17, end_col_offset=44, id='meeting_room', ctx=Load()),
                                                attr='is_published',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=18,
                                            col_offset=16,
                                            end_lineno=18,
                                            end_col_offset=110,
                                            targets=[Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=26, id='date_begin', ctx=Store())],
                                            value=Call(
                                                lineno=18,
                                                col_offset=29,
                                                end_lineno=18,
                                                end_col_offset=110,
                                                func=Name(lineno=18, col_offset=29, end_lineno=18, end_col_offset=44, id='format_datetime', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        lineno=18,
                                                        col_offset=45,
                                                        end_lineno=18,
                                                        end_col_offset=92,
                                                        value=Call(
                                                            lineno=18,
                                                            col_offset=45,
                                                            end_lineno=18,
                                                            end_col_offset=81,
                                                            func=Attribute(
                                                                lineno=18,
                                                                col_offset=45,
                                                                end_lineno=18,
                                                                end_col_offset=63,
                                                                value=Name(lineno=18, col_offset=45, end_lineno=18, end_col_offset=50, id='event', ctx=Load()),
                                                                attr='with_context',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    lineno=18,
                                                                    col_offset=64,
                                                                    end_lineno=18,
                                                                    end_col_offset=80,
                                                                    arg='tz',
                                                                    value=Attribute(
                                                                        lineno=18,
                                                                        col_offset=67,
                                                                        end_lineno=18,
                                                                        end_col_offset=80,
                                                                        value=Name(lineno=18, col_offset=67, end_lineno=18, end_col_offset=72, id='event', ctx=Load()),
                                                                        attr='date_tz',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='date_begin',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        lineno=18,
                                                        col_offset=94,
                                                        end_lineno=18,
                                                        end_col_offset=109,
                                                        arg='format',
                                                        value=Constant(lineno=18, col_offset=101, end_lineno=18, end_col_offset=109, value='medium', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            lineno=20,
                                            col_offset=16,
                                            end_lineno=23,
                                            end_col_offset=17,
                                            targets=[
                                                Subscript(
                                                    lineno=20,
                                                    col_offset=16,
                                                    end_lineno=20,
                                                    end_col_offset=39,
                                                    value=Name(lineno=20, col_offset=16, end_lineno=20, end_col_offset=22, id='values', ctx=Load()),
                                                    slice=Constant(lineno=20, col_offset=23, end_lineno=20, end_col_offset=38, value='toast_message', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                lineno=21,
                                                col_offset=20,
                                                end_lineno=22,
                                                end_col_offset=80,
                                                left=Call(
                                                    lineno=21,
                                                    col_offset=20,
                                                    end_lineno=21,
                                                    end_col_offset=93,
                                                    func=Name(lineno=21, col_offset=20, end_lineno=21, end_col_offset=21, id='_', ctx=Load()),
                                                    args=[Constant(lineno=21, col_offset=22, end_lineno=21, end_col_offset=92, value='The event %s starts on %s (%s). \nJoin us there to chat about "%s" !', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    lineno=22,
                                                    col_offset=22,
                                                    end_lineno=22,
                                                    end_col_offset=80,
                                                    elts=[
                                                        Attribute(
                                                            lineno=22,
                                                            col_offset=23,
                                                            end_lineno=22,
                                                            end_col_offset=33,
                                                            value=Name(lineno=22, col_offset=23, end_lineno=22, end_col_offset=28, id='event', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Name(lineno=22, col_offset=35, end_lineno=22, end_col_offset=45, id='date_begin', ctx=Load()),
                                                        Attribute(
                                                            lineno=22,
                                                            col_offset=47,
                                                            end_lineno=22,
                                                            end_col_offset=60,
                                                            value=Name(lineno=22, col_offset=47, end_lineno=22, end_col_offset=52, id='event', ctx=Load()),
                                                            attr='date_tz',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            lineno=22,
                                                            col_offset=62,
                                                            end_lineno=22,
                                                            end_col_offset=79,
                                                            value=Name(lineno=22, col_offset=62, end_lineno=22, end_col_offset=74, id='meeting_room', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=21,
                            value=Name(lineno=25, col_offset=15, end_lineno=25, end_col_offset=21, id='values', ctx=Load()),
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