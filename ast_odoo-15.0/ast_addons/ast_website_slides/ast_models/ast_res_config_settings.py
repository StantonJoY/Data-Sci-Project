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
            end_lineno=14,
            end_col_offset=65,
            name='ResConfigSettings',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=24,
                    end_lineno=7,
                    end_col_offset=45,
                    value=Name(lineno=7, col_offset=24, end_lineno=7, end_col_offset=30, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=36,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=36, value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=113,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=32, id='website_slide_google_app_key', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=35,
                        end_lineno=10,
                        end_col_offset=113,
                        func=Attribute(
                            lineno=10,
                            col_offset=35,
                            end_lineno=10,
                            end_col_offset=46,
                            value=Name(lineno=10, col_offset=35, end_lineno=10, end_col_offset=41, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=47,
                                end_lineno=10,
                                end_col_offset=96,
                                arg='related',
                                value=Constant(lineno=10, col_offset=55, end_lineno=10, end_col_offset=96, value='website_id.website_slide_google_app_key', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=98,
                                end_lineno=10,
                                end_col_offset=112,
                                arg='readonly',
                                value=Constant(lineno=10, col_offset=107, end_lineno=10, end_col_offset=112, value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=75,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=30, id='module_website_sale_slides', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=33,
                        end_lineno=11,
                        end_col_offset=75,
                        func=Attribute(
                            lineno=11,
                            col_offset=33,
                            end_lineno=11,
                            end_col_offset=47,
                            value=Name(lineno=11, col_offset=33, end_lineno=11, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=48,
                                end_lineno=11,
                                end_col_offset=74,
                                arg='string',
                                value=Constant(lineno=11, col_offset=55, end_lineno=11, end_col_offset=74, value='Sell on eCommerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=64,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=31, id='module_website_slides_forum', ctx=Store())],
                    value=Call(
                        lineno=12,
                        col_offset=34,
                        end_lineno=12,
                        end_col_offset=64,
                        func=Attribute(
                            lineno=12,
                            col_offset=34,
                            end_lineno=12,
                            end_col_offset=48,
                            value=Name(lineno=12, col_offset=34, end_lineno=12, end_col_offset=40, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=12,
                                col_offset=49,
                                end_lineno=12,
                                end_col_offset=63,
                                arg='string',
                                value=Constant(lineno=12, col_offset=56, end_lineno=12, end_col_offset=63, value='Forum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=13,
                    col_offset=4,
                    end_lineno=13,
                    end_col_offset=74,
                    targets=[Name(lineno=13, col_offset=4, end_lineno=13, end_col_offset=32, id='module_website_slides_survey', ctx=Store())],
                    value=Call(
                        lineno=13,
                        col_offset=35,
                        end_lineno=13,
                        end_col_offset=74,
                        func=Attribute(
                            lineno=13,
                            col_offset=35,
                            end_lineno=13,
                            end_col_offset=49,
                            value=Name(lineno=13, col_offset=35, end_lineno=13, end_col_offset=41, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=13,
                                col_offset=50,
                                end_lineno=13,
                                end_col_offset=73,
                                arg='string',
                                value=Constant(lineno=13, col_offset=57, end_lineno=13, end_col_offset=73, value='Certifications', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=65,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=30, id='module_mass_mailing_slides', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=33,
                        end_lineno=14,
                        end_col_offset=65,
                        func=Attribute(
                            lineno=14,
                            col_offset=33,
                            end_lineno=14,
                            end_col_offset=47,
                            value=Name(lineno=14, col_offset=33, end_lineno=14, end_col_offset=39, id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=48,
                                end_lineno=14,
                                end_col_offset=64,
                                arg='string',
                                value=Constant(lineno=14, col_offset=55, end_lineno=14, end_col_offset=64, value='Mailing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)