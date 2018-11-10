package com.riyenas0925.mvcboard.login.controller;


import org.springframework.security.access.annotation.Secured;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


@RequestMapping("/login/*")
@Controller
public class SampleController {
    private static final Logger logger = LoggerFactory.getLogger(SampleController.class);

    @GetMapping("/all")
    public void doAll() {

        logger.info("do all can access everybody");
    }

    @GetMapping("/member")
    public void doMember() {

        logger.info("logined member");
    }

    @GetMapping("/admin")
    public void doAdmin() {

        logger.info("admin only");
    }


    @PreAuthorize("hasAnyRole('ROLE_ADMIN','ROLE_MEMBER')")
    @GetMapping("/annoMember")
    public void doMember2() {

        logger.info("logined annotation member");
    }


    @Secured({"ROLE_ADMIN"})
    @GetMapping("/annoAdmin")
    public void doAdmin2() {

        logger.info("admin annotaion only");
    }
}
